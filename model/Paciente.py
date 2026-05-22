from model.Pessoa import Pessoa
import datetime

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, dataNascimento: datetime.date):
        super().__init__(nome, celular, cpf)
        self.dataNascimento = dataNascimento
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        if not isinstance(dataNascimento, datetime.date):
            raise ValueError("A data de nascimento deve ser do tipo datetime.date.")
        self.__dataNascimento = dataNascimento