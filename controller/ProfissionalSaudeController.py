from model.ProfissionalSaude import ProfissionalSaude
from view.ProfissionalSaudeView import ProfissionalSaudeView


class ProfissionalSaudeController:
    def __init__(self, profissionais):
        self.profissionais = profissionais
        self.view = None

    def abrirTela(self):
        self.view = ProfissionalSaudeView(self)
        self.listar()

    def incluir(self):
        try:
            nome, celular, cpf, especialidade, registro = self.view.lerDados()

            profissional = ProfissionalSaude(nome, celular, cpf, especialidade, registro)
            self.profissionais.append(profissional)

            self.view.mostrarMensagem("Profissional cadastrado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except ValueError as e:
            self.view.mostrarErro(f"Erro ao cadastrar profissional: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.profissionais)

    def alterar(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            profissional = self.profissionais[indice]

            nome, celular, cpf, especialidade, registro = self.view.lerDados()

            profissional.nome = nome
            profissional.celular = celular
            profissional.cpf = cpf
            profissional.especialidade = especialidade
            profissional.registroProfissional = registro

            self.view.mostrarMensagem("Profissional alterado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar profissional: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            profissional = self.profissionais.pop(indice)

            self.view.mostrarMensagem(f"Profissional excluído com sucesso: {profissional.nome}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir profissional: {e}")