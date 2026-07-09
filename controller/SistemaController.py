from controller.ClinicaController import ClinicaController
from controller.PacienteController import PacienteController
from controller.ProfissionalSaudeController import ProfissionalSaudeController
from controller.TipoAtendimentoController import TipoAtendimentoController
from controller.AtendimentoController import AtendimentoController
from controller.PagamentoController import PagamentoController
import os

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

        self.atendimentos = []
        self.atendimento_controller = AtendimentoController(
            self.atendimentos,
            self.clinicas,
            self.pacientes,
            self.profissionais,
            self.tipos_atendimento
        )

        self.pagamentos = []
        self.pagamento_controller = PagamentoController(
            self.pagamentos,
            self.atendimentos
        )
    
    def limparTela(self):
         os.system('cls')

    def iniciarSistema(self):
        while True:
            self.limparTela()
            self.view.mostrarMenuPrincipal()
            opcao = self.view.lerOpcao()

            if opcao == "1":
                self.abrirMenuCadastros()
            elif opcao == "2":
                self.abrirMenuRegistros()
            elif opcao == "3":
                self.abrirMenuRelatorios()
            elif opcao == "0":
                self.view.mostrarMensagem("Saindo...")
                break
            else:
                self.view.mostrarMensagem("Opção inválida.")

    def abrirMenuCadastros(self):
        while True:
            self.limparTela()
            print("\n=== CADASTROS ===")
            print("1 - Clinicas")
            print("2 - Pacientes")
            print("3 - Profissionais de Saúde")
            print("4 - Tipos de Atendimento")
            print("0 - Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menuClinicas()
            elif opcao == "2":
                self.menuPacientes()
            elif opcao == "3":
                self.menuProfissionalSaude()
            elif opcao == "4":
                self.menuTipoAtendimento()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def menuClinicas(self):
        self.clinica_controller.abrirTela()

    def menuPacientes(self):
        self.paciente_controller.abrirTela()

    def menuProfissionalSaude(self):
        self.profissional_controller.abrirTela()

    def menuTipoAtendimento(self):
        self.tipo_atendimento_controller.abrirTela()
    
    def abrirMenuRegistros(self):
        while True:
            self.limparTela()
            self.view.mostrarMenuRegistros()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            elif opcao == "1":
                self.menuAtendimento()
            elif opcao == "2":
                self.menuPagamentos()
            else:
                print("Opção invalida.")

    def menuAtendimento(self):
        while True:
            print("\n=== MENU ATENDIMENTO ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("5 - Adicionar Procedimento")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                    self.atendimento_controller.incluir()
            elif opcao == "2":
                    self.atendimento_controller.listar()
            elif opcao == "3":
                    self.atendimento_controller.alterar()
            elif opcao == "4":
                    self.atendimento_controller.excluir()
            elif opcao == "5":
                    self.atendimento_controller.adicionarProcedimento()
            elif opcao == "0":
                    break
            else:
                    print("Opção invalida.")
    def menuPagamentos(self):
        while True:
            print("\n=== MENU PAGAMENTOS ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                    self.pagamento_controller.incluir()
            elif opcao == "2":
                    self.pagamento_controller.listar()
            elif opcao == "3":
                    self.pagamento_controller.alterar()
            elif opcao == "4":
                    self.pagamento_controller.excluir()
            elif opcao == "0":
                    break
            else:
                    print("Opção inválida.")

    def abrirMenuRelatorios(self):
        while True:
            self.limparTela()
            self.view.mostrarMenuRelatorios()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            elif opcao == "1":
                self.relatorioClinicasComMaisAtendimentos()
            elif opcao == "2":
                self.relatorioAtendimentosMaisCarosEBaratos()
            elif opcao == "3":
                self.relatorioProcedimentosMaisRealizados()
            elif opcao == "4":
                self.relatorioProcedimentosMaisCarosEBaratos()
            else:
                self.view.mostrarMensagem("Opção inválida.")
    
    def relatorioClinicasComMaisAtendimentos(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        contagem = {}

        for atendimento in self.atendimentos:
            nome_clinica = atendimento.clinica.nome
            if nome_clinica in contagem:
                contagem[nome_clinica] += 1
            else:
                contagem[nome_clinica] = 1

        maior = max(contagem.values())

        print("\n=== CLINICAS COM MAIS ATENDIMENTOS ===")
        for clinica, quantidade in contagem.items():
            if quantidade == maior:
                print(clinica, "-", quantidade, "atendimentos")
    
    def relatorioAtendimentosMaisCarosEBaratos(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        mais_caro = self.atendimentos[0]
        mais_barato = self.atendimentos[0]

        for atendimento in self.atendimentos:
            if atendimento.valor > mais_caro.valor:
                mais_caro = atendimento
            if atendimento.valor < mais_barato.valor:
                mais_barato = atendimento

        print("\n=== ATENDIMENTO MAIS CARO ===")
        print(mais_caro.paciente.nome, "-", mais_caro.clinica.nome, "-", mais_caro.valor)

        print("\n=== ATENDIMENTO MAIS BARATO ===")
        print(mais_barato.paciente.nome, "-", mais_barato.clinica.nome, "-", mais_barato.valor)
    
    def relatorioProcedimentosMaisRealizados(self):
        contagem = {}

        for atendimento in self.atendimentos:
            for procedimento in atendimento.procedimentos:
                descricao = procedimento.descricao
                if descricao in contagem:
                    contagem[descricao] += 1
                else:
                    contagem[descricao] = 1

        if len(contagem) == 0:
            print("Nenhum procedimento cadastrado.")
            return

        maior = max(contagem.values())

        print("\n=== PROCEDIMENTOS MAIS REALIZADOS ===")
        for descricao, quantidade in contagem.items():
            if quantidade == maior:
                print(descricao, "-", quantidade, "vezes")
        
    def relatorioProcedimentosMaisCarosEBaratos(self):
        procedimentos = []

        for atendimento in self.atendimentos:
            for procedimento in atendimento.procedimentos:
                procedimentos.append(procedimento)

        if len(procedimentos) == 0:
            print("Nenhum procedimento cadastrado.")
            return

        mais_caro = procedimentos[0]
        mais_barato = procedimentos[0]

        for procedimento in procedimentos:
            if procedimento.custo > mais_caro.custo:
                mais_caro = procedimento
            if procedimento.custo < mais_barato.custo:
                mais_barato = procedimento

        print("\n=== PROCEDIMENTO MAIS CARO ===")
        print(mais_caro.descricao, "-", mais_caro.custo)

        print("\n=== PROCEDIMENTO MAIS BARATO ===")
        print(mais_barato.descricao, "-", mais_barato.custo)
            