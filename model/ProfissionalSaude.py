from model.Pessoa import Pessoa

class ProfissionalSaude(Pessoa):
    def __init__(self, nome: str, cpf: str, celular: str, especialidade: str, registroProfissional: str):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registroProfissional = registroProfissional
    
    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, especialidade):
        if isinstance(especialidade, str) and len(especialidade) < 3:
            raise ValueError("A especialidade deve conter pelo menos 3 caracteres.")
        self.__especialidade = especialidade

    @property
    def registroProfissional(self):
        return self.__registroProfissional

    @registroProfissional.setter
    def registroProfissional(self, registroProfissional):
        if isinstance(registroProfissional, str) and len(registroProfissional) < 5:
            raise ValueError("O registro profissional deve conter pelo menos 5 caracteres.")
        self.__registroProfissional = registroProfissional