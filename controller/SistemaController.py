from controller.ClinicaController import ClinicaController
from controller.PacienteController import PacienteController
from controller.ProfissionalSaudeController import ProfissionalSaudeController
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
        self.atendimentos = []
        self.pagamentos = []

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
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.menuClinicas()
            elif opcao == "2":
                self.menuPacientes()
            elif opcao == "3":
                self.menuProfissionalSaude()
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

    def abrirMenuRegistros(self):
        while True:
            self.view.mostrarMenuRegistros()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            else:
                self.view.mostrarMensagem("Modulo ainda em construção.")

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

    def abrirMenuRelatorios(self):
        while True:
            self.view.mostrarMenuRelatorios()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            else:
                self.view.mostrarMensagem("Modulo ainda em construção.")