class SistemaController:
    def __init__(self, view):
        self.view = view

        self.clinicas = []
        self.pacientes = []
        self.profissionais = []
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
            self.view.mostrarMenuCadastros()
            opcao = self.view.lerOpcao()

            if opcao == "0":
                break
            else:
                self.view.mostrarMensagem("Modulo ainda em construção.")

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