import datetime
from model.PagamentoDinheiro import PagamentoDinheiro
from model.PagamentoPix import PagamentoPix
from model.PagamentoCartaoCredito import PagamentoCartaoCredito
from dao.PagamentoDAO import PagamentoDAO


class PagamentoController:
    def __init__(self, pagamentos, atendimentos):
        self.dao = PagamentoDAO()
        self.pagamentos = self.dao.carregar()
        self.atendimentos = atendimentos

    def incluir(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        print("\nAtendimentos:")
        for i in range(len(self.atendimentos)):
            atendimento = self.atendimentos[i]
            print(i, "-", atendimento.paciente.nome, "-", atendimento.data, "-", atendimento.valor)

        try:
            indice_atendimento = int(input("Escolha o atendimento: "))
            atendimento = self.atendimentos[indice_atendimento]

            data = input("Data do pagamento (dd/mm/yyyy): ")
            data = datetime.datetime.strptime(data, "%d/%m/%Y").date()

            if data > atendimento.data:
                raise ValueError("O pagamento deve ser realizado ate a data do atendimento.")

            valor_pago = float(input("Valor do pagamento: "))

            print("\nTipo de pagamento:")
            print("1 - Dinheiro")
            print("2 - PIX")
            print("3 - Cartao de credito")
            tipo = input("Escolha uma opcao: ")

            if tipo == "1":
                pagamento = PagamentoDinheiro(data, valor_pago)
            elif tipo == "2":
                cpf_pagador = input("CPF do pagador: ")
                pagamento = PagamentoPix(cpf_pagador, data, valor_pago)
            elif tipo == "3":
                numero_cartao = input("Numero do cartao: ")
                bandeira = input("Bandeira: ")
                pagamento = PagamentoCartaoCredito(numero_cartao, bandeira, data, valor_pago)
            else:
                print("Opcao invalida.")
                return

            self.pagamentos.append(pagamento)

            if not hasattr(atendimento, "pagamentos"):
                atendimento.pagamentos = []

            atendimento.pagamentos.append(pagamento)

            self.dao.salvar(self.pagamentos)

            print("Pagamento cadastrado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao cadastrar pagamento:", e)

    def listar(self):
        if len(self.pagamentos) == 0:
            print("Nenhum pagamento cadastrado.")
            return

        print("\nLista de pagamentos:")
        for i in range(len(self.pagamentos)):
            pagamento = self.pagamentos[i]
            print(i, "-", pagamento.data, "-", pagamento.valorPago)

    def alterar(self):
        if len(self.pagamentos) == 0:
            print("Nenhum pagamento cadastrado.")
            return

        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        self.listar()

        try:
            indice_pagamento = int(input("Digite o indice do pagamento que deseja alterar: "))

            print("\nAtendimentos:")
            for i in range(len(self.atendimentos)):
                atendimento = self.atendimentos[i]
                print(i, "-", atendimento.paciente.nome, "-", atendimento.data, "-", atendimento.valor)

            indice_atendimento = int(input("Escolha o atendimento: "))
            atendimento = self.atendimentos[indice_atendimento]

            data = input("Nova data do pagamento (dd/mm/yyyy): ")
            data = datetime.datetime.strptime(data, "%d/%m/%Y").date()

            if data > atendimento.data:
                raise ValueError("O pagamento deve ser realizado ate a data do atendimento.")

            valor_pago = float(input("Novo valor do pagamento: "))

            print("\nTipo de pagamento:")
            print("1 - Dinheiro")
            print("2 - PIX")
            print("3 - Cartao de credito")
            tipo = input("Escolha uma opcao: ")

            if tipo == "1":
                novo_pagamento = PagamentoDinheiro(data, valor_pago)
            elif tipo == "2":
                cpf_pagador = input("CPF do pagador: ")
                novo_pagamento = PagamentoPix(cpf_pagador, data, valor_pago)
            elif tipo == "3":
                numero_cartao = input("Numero do cartao: ")
                bandeira = input("Bandeira: ")
                novo_pagamento = PagamentoCartaoCredito(numero_cartao, bandeira, data, valor_pago)
            else:
                print("Opcao invalida.")
                return

            self.pagamentos[indice_pagamento] = novo_pagamento

            if not hasattr(atendimento, "pagamentos"):
                atendimento.pagamentos = []

            atendimento.pagamentos.append(novo_pagamento)

            self.dao.salvar(self.pagamentos)

            print("Pagamento alterado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao alterar pagamento:", e)

    def excluir(self):
        if len(self.pagamentos) == 0:
            print("Nenhum pagamento cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do pagamento que deseja excluir: "))
            removido = self.pagamentos.pop(indice)
            self.dao.salvar(self.pagamentos)

            print("Pagamento excluido com sucesso:", removido.data, "-", removido.valorPago)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir pagamento:", e)