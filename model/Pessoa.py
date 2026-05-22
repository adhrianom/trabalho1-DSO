class Pessoa():
    def __init__(self, nome: str, celular: str, cpf: str):
        super().__init__()
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")
        if len(nome.strip()) < 3:
            raise ValueError("O nome deve conter pelo menos 3 caracteres.")
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        if not isinstance(celular, str):
            raise ValueError("O celular deve ser uma string.")
        if len(celular.strip()) < 8:
            raise ValueError("O celular deve conter pelo menos 8 caracteres.")
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if not isinstance(cpf, str):
            raise ValueError("O CPF deve ser uma string.")
        if len(cpf.strip()) != 11:
            raise ValueError("O CPF deve conter exatamente 11 caracteres.")
        self.__cpf = cpf
    
    