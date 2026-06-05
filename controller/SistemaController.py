from controller.ClinicaController import ClinicaController
from controller.PacienteController import PacienteController
from controller.ProfissionalSaudeController import ProfissionalSaudeController
from controller.TipoAtendimentoController import TipoAtendimentoController
from controller.AtendimentoController import AtendimentoController
from controller.PagamentoController import PagamentoController

class SistemaController:
    def __init__(self, view):
        self.view = view
        self.clinicas = []  
        self.clinica_controller = ClinicaController(self.clinicas)
        self.pacientes = []
        self.paciente_controller = PacienteController(self.pacientes)
        self.profissionais = []
        self.profissional_controller = ProfissionalSaudeController(self.profissionais)
        self.tipos_atendimento = []
        self.tipo_atendimento_controller = TipoAtendimentoController(self.tipos_atendimento)
        self.atendimentos = []
        self.atendimento_controller = AtendimentoController(
            self.atendimentos,
            self.clinicas,
            self.pacientes,
            self.profissionais,
            self.tipos_atendimento
        )
        self.pagamentos = []
        self.pagamento_controller = PagamentoController(self.pagamentos, self.atendimentos)
    def iniciarSistema(self):
        while True:
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
            print("\n=== CADASTROS ===")
            print("1 - Clinicas")
            print("2 - Pacientes")
            print("3 - Profissionais de Saúde")
            print("4 - Tipos de Atendimento")
            print("5 - Atendimentos")
            print("6 - Pagamentos")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.menuClinicas()
            elif opcao == "2":
                self.menuPacientes()
            elif opcao == "3":
                self.menuProfissionalSaude()
            elif opcao == "4":
                self.menuTipoAtendimento()
            elif opcao == "5":
                self.menuAtendimento()
            elif opcao == "6":
                self.menuPagamentos()
            elif opcao == "0":
                break
            else:
                print("Opcao invalida.")

    def menuClinicas(self):
        while True:
            print("\n=== MENU CLINICAS ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.clinica_controller.incluir()
            elif opcao == "2":
                self.clinica_controller.listar()
            elif opcao == "3":
                self.clinica_controller.alterar()
            elif opcao == "4":
                self.clinica_controller.excluir()
            elif opcao == "0":
                break
            else:
                print("Opcao invalida.")

    def menuPacientes(self):
        while True:
            print("\n=== MENU PACIENTES ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.paciente_controller.incluir()
            elif opcao == "2":
                self.paciente_controller.listar()
            elif opcao == "3":
                self.paciente_controller.alterar()
            elif opcao == "4":
                self.paciente_controller.excluir()
            elif opcao == "0":
                break
            else:
                print("Opcao invalida.")

    def menuProfissionalSaude(self):
        while True:
            print("\n=== MENU PROFISSIONAL DE SAÚDE ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.profissional_controller.incluir()
            elif opcao == "2":
                self.profissional_controller.listar()
            elif opcao == "3":
                self.profissional_controller.alterar()
            elif opcao == "4":
                self.profissional_controller.excluir()
            elif opcao == "0":
                break
            else:
                print("Opcao invalida.")

    def menuTipoAtendimento(self):
        while True:
            print("\n=== MENU TIPO DE ATENDIMENTO ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                    self.tipo_atendimento_controller.incluir()
            elif opcao == "2":
                    self.tipo_atendimento_controller.listar()
            elif opcao == "3":
                    self.tipo_atendimento_controller.alterar()
            elif opcao == "4":
                    self.tipo_atendimento_controller.excluir()
            elif opcao == "0":
                    break
            else:
                    print("Opcao invalida.")

    def menuAtendimento(self):
        while True:
            print("\n=== MENU ATENDIMENTO ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("5 - Adicionar Procedimento")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

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
                    print("Opcao invalida.")
    def menuPagamentos(self):
        while True:
            print("\n=== MENU PAGAMENTOS ===")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("0 - Voltar")

            opcao = input("Escolha uma opcao: ")

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
                    print("Opcao invalida.")
    
    def abrirMenuRegistros(self):
        while True:
            self.view.mostrarMenuRegistros()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            else:
                self.view.mostrarMensagem("Modulo ainda em construção.")

    def abrirMenuRelatorios(self):
        while True:
            self.view.mostrarMenuRelatorios()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            else:
                self.view.mostrarMensagem("Modulo ainda em construção.")