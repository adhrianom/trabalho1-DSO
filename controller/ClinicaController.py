from model.Clinica import Clinica
import datetime


class ClinicaController:
    def __init__(self, clinicas):
        self.clinicas = clinicas

    def incluir(self):
        try:
            nome = input("Nome da clinica: ")
            cidade = input("Cidade: ")
            descricao = input("Descricao: ")
            horario_abertura = input("Horario de abertura (HH:MM): ")
            horario_fechamento = input("Horario de fechamento (HH:MM): ")

            hora_abertura = datetime.datetime.strptime(horario_abertura, "%H:%M").time()
            hora_fechamento = datetime.datetime.strptime(horario_fechamento, "%H:%M").time()

            clinica = Clinica(nome, cidade, descricao, hora_abertura, hora_fechamento)
            self.clinicas.append(clinica)

            print("Clinica cadastrada com sucesso.")
        except ValueError as e:
            print("Erro ao cadastrar clinica:", e)

    def listar(self):
        if len(self.clinicas) == 0:
            print("Nenhuma clinica cadastrada.")
            return

        print("\nLista de clinicas:")
        for i in range(len(self.clinicas)):
            clinica = self.clinicas[i]
            print(i, "-", clinica.nome, "-", clinica.cidade, "-", clinica.descricao, "-", clinica.horarioAbertura.strftime("%H:%M"), "-", clinica.horarioFechamento.strftime("%H:%M"))

    def alterar(self):
        if len(self.clinicas) == 0:
            print("Nenhuma clinica cadastrada.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice da clinica que deseja alterar: "))
            clinica = self.clinicas[indice]

            nome = input("Novo nome: ")
            cidade = input("Nova cidade: ")
            descricao = input("Nova descricao: ")
            horario_abertura = input("Novo horario de abertura (HH:MM): ")
            horario_fechamento = input("Novo horario de fechamento (HH:MM): ")

            clinica.nome = nome
            clinica.cidade = cidade
            clinica.descricao = descricao
            clinica.horarioAbertura = datetime.datetime.strptime(horario_abertura, "%H:%M").time()
            clinica.horarioFechamento = datetime.datetime.strptime(horario_fechamento, "%H:%M").time()

            print("Clinica alterada com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao alterar clinica:", e)

    def excluir(self):
        if len(self.clinicas) == 0:
            print("Nenhuma clinica cadastrada.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice da clinica que deseja excluir: "))
            removida = self.clinicas.pop(indice)
            print("Clinica excluida com sucesso:", removida.nome)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir clinica:", e)