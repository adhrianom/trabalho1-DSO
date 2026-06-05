class SistemaView:
    def mostrarMenuPrincipal(self):
        print("\n=== SISTEMA DE CLINICAS ===")
        print("1 - Cadastros")
        print("2 - Registros")
        print("3 - Relatórios")
        print("0 - Sair")

    def mostrarMenuCadastros(self):
        print("\n=== CADASTROS ===")
        print("1 - Clinicas")
        print("2 - Pacientes")
        print("3 - Profissionais de Saúde")
        print("4 - Tipos de Atendimento")
        print("0 - Voltar")

    def mostrarMenuRegistros(self):
        print("\n=== REGISTROS ===")
        print("1 - Atendimentos")
        print("2 - Pagamentos")
        print("0 - Voltar")

    def mostrarMenuRelatorios(self):
        print("\n=== RELATÓRIOS ===")
        print("1 - Clinicas com mais atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")

    def lerOpcao(self):
        return input("Escolha uma opção: ")

    def mostrarMensagem(self, mensagem):
        print(mensagem)