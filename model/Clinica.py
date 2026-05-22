import datetime
class Clinica():
    def __init__(self, nome: str, cidade: str, descricao: str, horarioAbertura: datetime.time, horarioFechamento: datetime.time):
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.horarioAbertura = horarioAbertura
        self.horarioFechamento = horarioFechamento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("O nome da clínica não pode ser vazio.")
        self.__nome = value
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, value):
        if not value:
            raise ValueError("A cidade da clínica não pode ser vazia.")
        self.__cidade = value

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, value):
        if not value:
            raise ValueError("A descrição da clínica não pode ser vazia.")
        self.__descricao = value
    
    @property
    def horarioAbertura(self):
        return self.__horarioAbertura
    
    @horarioAbertura.setter
    def horarioAbertura(self, value):
        if not isinstance(value, datetime.time):
            raise ValueError("O horário de abertura deve ser do tipo datetime.time.")
        self.__horarioAbertura = value
    
    @property
    def horarioFechamento(self):
        return self.__horarioFechamento
    
    @horarioFechamento.setter
    def horarioFechamento(self, value):
        if not isinstance(value, datetime.time):
            raise ValueError("O horário de fechamento deve ser do tipo datetime.time.")
        self.__horarioFechamento = value