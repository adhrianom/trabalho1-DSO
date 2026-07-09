from model.TipoAtendimento import TipoAtendimento
from view.TipoAtendimentoView import TipoAtendimentoView
from dao.TipoAtendimentoDAO import TipoAtendimentoDAO


class TipoAtendimentoController:
    def __init__(self, tipos_atendimento=None):
        self.dao = TipoAtendimentoDAO()
        self.tipos_atendimento = self.dao.carregar()
        self.view = None

    def abrirTela(self):
        self.view = TipoAtendimentoView(self)
        self.listar()

    def incluir(self):
        try:
            descricao = self.view.lerDados()

            tipo = TipoAtendimento(descricao)
            self.tipos_atendimento.append(tipo)
            self.dao.salvar(self.tipos_atendimento)

            self.view.mostrarMensagem("Tipo de atendimento cadastrado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except ValueError as e:
            self.view.mostrarErro(f"Erro ao cadastrar tipo de atendimento: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.tipos_atendimento)

    def alterar(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            tipo = self.tipos_atendimento[indice]

            descricao = self.view.lerDados()
            tipo.descricao = descricao

            self.dao.salvar(self.tipos_atendimento)

            self.view.mostrarMensagem("Tipo de atendimento alterado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar tipo de atendimento: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            tipo = self.tipos_atendimento.pop(indice)
            self.dao.salvar(self.tipos_atendimento)

            self.view.mostrarMensagem(f"Tipo de atendimento excluído com sucesso: {tipo.descricao}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir tipo de atendimento: {e}")