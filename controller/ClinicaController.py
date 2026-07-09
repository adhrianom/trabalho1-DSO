from model.Clinica import Clinica
from view.ClinicaView import ClinicaView
from dao.ClinicaDAO import ClinicaDAO
import datetime


class ClinicaController:
    def __init__(self, clinicas=None):
        self.dao = ClinicaDAO()
        self.clinicas = self.dao.carregar()
        self.view = None

    def abrirTela(self):
        self.view = ClinicaView(self)
        self.listar()

    def incluir(self):
        try:
            nome, cidade, descricao, horario_abertura, horario_fechamento = self.view.lerDados()

            hora_abertura = datetime.datetime.strptime(horario_abertura, "%H:%M").time()
            hora_fechamento = datetime.datetime.strptime(horario_fechamento, "%H:%M").time()

            clinica = Clinica(nome, cidade, descricao, hora_abertura, hora_fechamento)
            self.clinicas.append(clinica)
            self.dao.salvar(self.clinicas)

            self.view.mostrarMensagem("Clínica cadastrada com sucesso.")
            self.view.limparCampos()
            self.listar()
        except ValueError as e:
            self.view.mostrarErro(f"Erro ao cadastrar clínica: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.clinicas)

    def alterar(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            clinica = self.clinicas[indice]

            nome, cidade, descricao, horario_abertura, horario_fechamento = self.view.lerDados()

            clinica.nome = nome
            clinica.cidade = cidade
            clinica.descricao = descricao
            clinica.horarioAbertura = datetime.datetime.strptime(horario_abertura, "%H:%M").time()
            clinica.horarioFechamento = datetime.datetime.strptime(horario_fechamento, "%H:%M").time()

            self.dao.salvar(self.clinicas)

            self.view.mostrarMensagem("Clínica alterada com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar clínica: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            clinica = self.clinicas.pop(indice)
            self.dao.salvar(self.clinicas)

            self.view.mostrarMensagem(f"Clínica excluída com sucesso: {clinica.nome}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir clínica: {e}")