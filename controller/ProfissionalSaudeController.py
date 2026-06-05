from model.ProfissionalSaude import ProfissionalSaude
import datetime


class ProfissionalSaudeController:
    def __init__(self, profissionais, ):
        self.profissionais = profissionais


    def incluir(self):
        try:
            nome = input("Nome do Profissional de Saúde: ")
            celular = input("Celular: ")
            cpf = input("CPF: ")
            especialidade = input("Especialidade: ")
            registroProfissional = input("Registro Profissional: ")

            profissional = ProfissionalSaude(nome, cpf, celular, especialidade, registroProfissional)
            self.profissionais.append(profissional)

            print("Profissional de saúde cadastrado com sucesso.")
        except ValueError as e:
            print("Erro ao cadastrar profissional de saúde:", e)

    def listar(self):
        if len(self.profissionais) == 0:
            print("Nenhum profissional de saúde cadastrado.")
            return

        print("\nLista de profissionais de saúde:")
        for i in range(len(self.profissionais)):
            profissional = self.profissionais[i]
            print(i, "-", profissional.nome, "-", profissional.celular, "-", profissional.cpf, "-", profissional.especialidade, "-", profissional.registroProfissional)

    def alterar(self):
        if len(self.profissionais) == 0:
            print("Nenhum profissional de saúde cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do profissional que deseja alterar: "))
            profissional = self.profissionais[indice]

            nome = input("Novo nome: ")
            celular = input("Novo celular: ")
            cpf = input("Novo CPF: ")
            especialidade = input("Nova especialidade: ")
            registroProfissional = input("Novo registro profissional: ")

            profissional.nome = nome
            profissional.celular = celular
            profissional.cpf = cpf
            profissional.especialidade = especialidade
            profissional.registroProfissional = registroProfissional

            print("Profissional de saúde alterado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao alterar profissional de saúde:", e)

    def excluir(self):
        if len(self.profissionais) == 0:
            print("Nenhum profissional de saúde cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do profissional que deseja excluir: "))
            removido = self.profissionais.pop(indice)
            print("Profissional de saúde excluido com sucesso:", removido.nome)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir paciente:", e)