import datetime
from model.PagamentoDinheiro import PagamentoDinheiro
from model.PagamentoPix import PagamentoPix
from model.PagamentoCartaoCredito import PagamentoCartaoCredito
from view.PagamentoView import PagamentoView
from dao.PagamentoDAO import PagamentoDAO


class PagamentoController:
    def __init__(self, pagamentos, atendimentos):
        self.dao = PagamentoDAO()
        self.pagamentos = self.dao.carregar()
        self.atendimentos = atendimentos
        self.view = None

    def abrirTela(self):
        self.view = PagamentoView(self)
        self.view.atualizarCombos(self.atendimentos)
        self.listar()

    def incluir(self):
        if len(self.atendimentos) == 0:
            self.view.mostrarErro("Nenhum atendimento cadastrado.")
            return

        try:
            indice_atendimento, data_str, valor_str, tipo, cpf_pagador, numero_cartao, bandeira = self.view.lerDados()

            if indice_atendimento < 0:
                raise ValueError("Selecione um atendimento.")

            atendimento = self.atendimentos[indice_atendimento]

            data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            if data > atendimento.data:
                raise ValueError("O pagamento deve ser realizado até a data do atendimento.")

            valor_pago = float(valor_str)

            if tipo == "Dinheiro":
                pagamento = PagamentoDinheiro(data, valor_pago)

            elif tipo == "PIX":
                pagamento = PagamentoPix(cpf_pagador, data, valor_pago)

            elif tipo == "Cartão de Crédito":
                pagamento = PagamentoCartaoCredito(numero_cartao, bandeira, data, valor_pago)

            else:
                raise ValueError("Selecione o tipo de pagamento.")

            self.pagamentos.append(pagamento)

            if not hasattr(atendimento, "pagamentos"):
                atendimento.pagamentos = []

            atendimento.pagamentos.append(pagamento)

            self.dao.salvar(self.pagamentos)

            self.view.mostrarMensagem("Pagamento cadastrado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao cadastrar pagamento: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.pagamentos)

    def alterar(self):
        if len(self.pagamentos) == 0:
            self.view.mostrarErro("Nenhum pagamento cadastrado.")
            return

        if len(self.atendimentos) == 0:
            self.view.mostrarErro("Nenhum atendimento cadastrado.")
            return

        try:
            indice_pagamento = self.view.lerIndiceSelecionado()
            indice_atendimento, data_str, valor_str, tipo, cpf_pagador, numero_cartao, bandeira = self.view.lerDados()

            if indice_atendimento < 0:
                raise ValueError("Selecione um atendimento.")

            atendimento = self.atendimentos[indice_atendimento]

            data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            if data > atendimento.data:
                raise ValueError("O pagamento deve ser realizado até a data do atendimento.")

            valor_pago = float(valor_str)

            if tipo == "Dinheiro":
                novo_pagamento = PagamentoDinheiro(data, valor_pago)

            elif tipo == "PIX":
                novo_pagamento = PagamentoPix(cpf_pagador, data, valor_pago)

            elif tipo == "Cartão de Crédito":
                novo_pagamento = PagamentoCartaoCredito(numero_cartao, bandeira, data, valor_pago)

            else:
                raise ValueError("Selecione o tipo de pagamento.")

            self.pagamentos[indice_pagamento] = novo_pagamento

            if not hasattr(atendimento, "pagamentos"):
                atendimento.pagamentos = []

            atendimento.pagamentos.append(novo_pagamento)

            self.dao.salvar(self.pagamentos)

            self.view.mostrarMensagem("Pagamento alterado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar pagamento: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            pagamento = self.pagamentos.pop(indice)

            self.dao.salvar(self.pagamentos)

            self.view.mostrarMensagem(f"Pagamento excluído com sucesso: {pagamento.valorPago}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir pagamento: {e}")