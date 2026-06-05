from model.TipoAtendimento import TipoAtendimento


class TipoAtendimentoController:
    def __init__(self, tipos_atendimento):
        self.tipos_atendimento = tipos_atendimento


    def incluir(self):
        try:
            descricao = input("Descrição: ")

            tipo_atendimento = TipoAtendimento(descricao)
            self.tipos_atendimento.append(tipo_atendimento)

            print("Tipo de atendimento cadastrado com sucesso.")
        except ValueError as e:
            print("Erro ao cadastrar tipo de atendimento:", e)

    def listar(self):
        if len(self.tipos_atendimento) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return

        print("\nLista de tipos de atendimento:")
        for i in range(len(self.tipos_atendimento)):
            tipo_atendimento = self.tipos_atendimento[i]
            print(i, "-", tipo_atendimento.descricao)

    def alterar(self):
        if len(self.tipos_atendimento) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do tipo de atendimento que deseja alterar: "))
            tipo_atendimento = self.tipos_atendimento[indice]

            descricao = input("Nova descrição: ")

            tipo_atendimento.descricao = descricao

            print("Tipo de atendimento alterado com sucesso.")
    
        except (ValueError, IndexError) as e:
            print("Erro ao alterar tipo de atendimento:", e)

    def excluir(self):
        if len(self.tipos_atendimento) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do tipo de atendimento que deseja excluir: "))
            removido = self.tipos_atendimento.pop(indice)
            print("Tipo de atendimento excluido com sucesso:", removido.descricao)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir tipo de atendimento:", e)