from controller.ClinicaController import ClinicaController
from controller.PacienteController import PacienteController
from controller.ProfissionalSaudeController import ProfissionalSaudeController
from controller.TipoAtendimentoController import TipoAtendimentoController
from controller.AtendimentoController import AtendimentoController
from controller.PagamentoController import PagamentoController
from view.RelatorioView import RelatorioView


class SistemaController:
    def __init__(self, view):
        self.view = view

        self.clinica_controller = ClinicaController()
        self.clinicas = self.clinica_controller.clinicas

        self.paciente_controller = PacienteController()
        self.pacientes = self.paciente_controller.pacientes

        self.profissional_controller = ProfissionalSaudeController()
        self.profissionais = self.profissional_controller.profissionais

        self.tipo_atendimento_controller = TipoAtendimentoController()
        self.tipos_atendimento = self.tipo_atendimento_controller.tipos_atendimento

        self.atendimento_controller = AtendimentoController(
            [],
            self.clinicas,
            self.pacientes,
            self.profissionais,
            self.tipos_atendimento
        )
        self.atendimentos = self.atendimento_controller.atendimentos

        self.pagamento_controller = PagamentoController(
            [],
            self.atendimentos
        )
        self.pagamentos = self.pagamento_controller.pagamentos

        self.relatorio_view = None

    def menuClinicas(self):
        self.clinica_controller.abrirTela()

    def menuPacientes(self):
        self.paciente_controller.abrirTela()

    def menuProfissionalSaude(self):
        self.profissional_controller.abrirTela()

    def menuTipoAtendimento(self):
        self.tipo_atendimento_controller.abrirTela()

    def menuAtendimento(self):
        self.atendimento_controller.abrirTela()

    def menuPagamentos(self):
        self.pagamento_controller.abrirTela()

    def abrirMenuRelatorios(self):
        self.relatorio_view = RelatorioView(self)

    def relatorioClinicasComMaisAtendimentos(self):
        if len(self.atendimentos) == 0:
            return "Nenhum atendimento cadastrado."

        contagem = {}

        for atendimento in self.atendimentos:
            nome_clinica = atendimento.clinica.nome

            if nome_clinica in contagem:
                contagem[nome_clinica] += 1
            else:
                contagem[nome_clinica] = 1

        maior = max(contagem.values())

        resultado = "=== CLINICAS COM MAIS ATENDIMENTOS ===\n\n"

        for clinica, quantidade in contagem.items():
            if quantidade == maior:
                resultado += f"{clinica} - {quantidade} atendimento(s)\n"

        return resultado

    def relatorioAtendimentosMaisCarosEBaratos(self):
        if len(self.atendimentos) == 0:
            return "Nenhum atendimento cadastrado."

        mais_caro = self.atendimentos[0]
        mais_barato = self.atendimentos[0]

        for atendimento in self.atendimentos:
            if atendimento.valor > mais_caro.valor:
                mais_caro = atendimento

            if atendimento.valor < mais_barato.valor:
                mais_barato = atendimento

        resultado = "=== ATENDIMENTO MAIS CARO ===\n\n"
        resultado += f"Paciente: {mais_caro.paciente.nome}\n"
        resultado += f"Clinica: {mais_caro.clinica.nome}\n"
        resultado += f"Data: {mais_caro.data.strftime('%d/%m/%Y')}\n"
        resultado += f"Valor: R$ {mais_caro.valor:.2f}\n\n"

        resultado += "=== ATENDIMENTO MAIS BARATO ===\n\n"
        resultado += f"Paciente: {mais_barato.paciente.nome}\n"
        resultado += f"Clinica: {mais_barato.clinica.nome}\n"
        resultado += f"Data: {mais_barato.data.strftime('%d/%m/%Y')}\n"
        resultado += f"Valor: R$ {mais_barato.valor:.2f}\n"

        return resultado

    def relatorioProcedimentosMaisRealizados(self):
        contagem = {}

        for atendimento in self.atendimentos:
            procedimentos = getattr(atendimento, "procedimentos", [])

            for procedimento in procedimentos:
                descricao = procedimento.descricao

                if descricao in contagem:
                    contagem[descricao] += 1
                else:
                    contagem[descricao] = 1

        if len(contagem) == 0:
            return "Nenhum procedimento cadastrado."

        maior = max(contagem.values())

        resultado = "=== PROCEDIMENTOS MAIS REALIZADOS ===\n\n"

        for descricao, quantidade in contagem.items():
            if quantidade == maior:
                resultado += f"{descricao} - {quantidade} vez(es)\n"

        return resultado

    def relatorioProcedimentosMaisCarosEBaratos(self):
        procedimentos = []

        for atendimento in self.atendimentos:
            procedimentos_atendimento = getattr(atendimento, "procedimentos", [])

            for procedimento in procedimentos_atendimento:
                procedimentos.append(procedimento)

        if len(procedimentos) == 0:
            return "Nenhum procedimento cadastrado."

        mais_caro = procedimentos[0]
        mais_barato = procedimentos[0]

        for procedimento in procedimentos:
            if procedimento.custo > mais_caro.custo:
                mais_caro = procedimento

            if procedimento.custo < mais_barato.custo:
                mais_barato = procedimento

        resultado = "=== PROCEDIMENTO MAIS CARO ===\n\n"
        resultado += f"Descricao: {mais_caro.descricao}\n"
        resultado += f"Custo: R$ {mais_caro.custo:.2f}\n\n"

        resultado += "=== PROCEDIMENTO MAIS BARATO ===\n\n"
        resultado += f"Descricao: {mais_barato.descricao}\n"
        resultado += f"Custo: R$ {mais_barato.custo:.2f}\n"

        return resultado