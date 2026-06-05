from model.Paciente import Paciente
import datetime


class PacienteController:
    def __init__(self, pacientes):
        self.pacientes = pacientes

    def incluir(self):
        try:
            nome = input("Nome do paciente: ")
            celular = input("Celular: ")
            cpf = input("CPF: ")
            data_str = input("Data de nascimento (DD/MM/YYYY): ")
            dataNascimento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            paciente = Paciente(nome, celular, cpf, dataNascimento)
            self.pacientes.append(paciente)

            print("Paciente cadastrado com sucesso.")
        except ValueError as e:
            print("Erro ao cadastrar paciente:", e)

    def listar(self):
        if len(self.pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return

        print("\nLista de pacientes:")
        for i in range(len(self.pacientes)):
            paciente = self.pacientes[i]
            print(i, "-", paciente.nome, "-", paciente.celular, "-", paciente.cpf, "-", paciente.dataNascimento.strftime("%d/%m/%Y"))

    def alterar(self):
        if len(self.pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do paciente que deseja alterar: "))
            paciente = self.pacientes[indice]

            nome = input("Novo nome: ")
            celular = input("Novo celular: ")
            cpf = input("Novo CPF: ")
            data_str = input("Nova data de nascimento (DD/MM/YYYY): ")

            paciente.nome = nome
            paciente.celular = celular
            paciente.cpf = cpf
            paciente.dataNascimento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            print("Paciente alterado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao alterar paciente:", e)

    def excluir(self):
        if len(self.pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o indice do paciente que deseja excluir: "))
            removido = self.pacientes.pop(indice)
            print("Paciente excluido com sucesso:", removido.nome)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir paciente:", e)