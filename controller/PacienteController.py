from model.Paciente import Paciente
from view.PacienteView import PacienteView
import datetime


class PacienteController:
    def __init__(self, pacientes):
        self.pacientes = pacientes
        self.view = None

    def abrirTela(self):
        self.view = PacienteView(self)
        self.listar()

    def incluir(self):
        try:
            nome, celular, cpf, data_str = self.view.lerDados()
            data_nascimento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            paciente = Paciente(nome, celular, cpf, data_nascimento)
            self.pacientes.append(paciente)

            self.view.mostrarMensagem("Paciente cadastrado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except ValueError as e:
            self.view.mostrarErro(f"Erro ao cadastrar paciente: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.pacientes)

    def alterar(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            paciente = self.pacientes[indice]

            nome, celular, cpf, data_str = self.view.lerDados()

            paciente.nome = nome
            paciente.celular = celular
            paciente.cpf = cpf
            paciente.dataNascimento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            self.view.mostrarMensagem("Paciente alterado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar paciente: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            paciente = self.pacientes.pop(indice)

            self.view.mostrarMensagem(f"Paciente excluído com sucesso: {paciente.nome}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir paciente: {e}")