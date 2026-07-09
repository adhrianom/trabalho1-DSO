import os
import pickle


class BaseDAO:
    def __init__(self, nome_arquivo):
        pasta_atual = os.path.dirname(__file__)
        pasta_dados = os.path.join(pasta_atual, "..", "dados")

        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)

        self.caminho_arquivo = os.path.join(pasta_dados, nome_arquivo)

    def salvar(self, lista):
        with open(self.caminho_arquivo, "wb") as arquivo:
            pickle.dump(lista, arquivo)

    def carregar(self):
        if os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "rb") as arquivo:
                return pickle.load(arquivo)
        return []