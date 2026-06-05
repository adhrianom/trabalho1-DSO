import datetime
from model.Clinica import Clinica
from model.Paciente import Paciente
from model.ProfissionalSaude import ProfissionalSaude
from model.TipoAtendimento import TipoAtendimento

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissionalSaude: ProfissionalSaude, tipoAtendimento: TipoAtendimento, data: datetime.date, horaInicio: datetime.time, horaFim: datetime.time, valor: float):
        self.clinica = clinica
        self.paciente = paciente
        self.profissionalSaude = profissionalSaude
        self.tipoAtendimento = tipoAtendimento
        self.data = data
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.valor = valor
        self.procedimentos = []
        self.pagamentos = []

    @property
    def clinica(self):
        return self.__clinica
    
    @clinica.setter
    def clinica(self, value):
        if not isinstance(value, Clinica):
            raise ValueError("A clínica deve ser do tipo Clinica")
        self.__clinica = value

    @property
    def paciente(self):
        return self.__paciente
    
    @paciente.setter
    def paciente(self, value):
        if not isinstance(value, Paciente):
            raise ValueError("O paciente deve ser do tipo Paciente")
        self.__paciente = value
    
    @property
    def profissionalSaude(self):
        return self.__profissionalSaude
    
    @profissionalSaude.setter
    def profissionalSaude(self, value):
        if not isinstance(value, ProfissionalSaude):
            raise ValueError("O profissional de saúde deve ser do tipo ProfissionalSaude")
        self.__profissionalSaude = value

    @property
    def tipoAtendimento(self):
        return self.__tipoAtendimento
    
    @tipoAtendimento.setter
    def tipoAtendimento(self, value):
        if not isinstance(value, TipoAtendimento):
            raise ValueError("O tipo de atendimento deve ser do tipo TipoAtendimento")
        self.__tipoAtendimento = value

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("A data deve ser do tipo datetime.date")
        self.__data = value 

    @property
    def horaInicio(self):
        return self.__horaInicio
        
    @horaInicio.setter
    def horaInicio(self, value):
        if not isinstance(value, datetime.time):
            raise ValueError("A hora de início deve ser do tipo datetime.time")
        self.__horaInicio = value

    @property
    def horaFim(self):
        return self.__horaFim
    
    @horaFim.setter
    def horaFim(self, value):
        if not isinstance(value, datetime.time):
            raise ValueError("A hora de fim deve ser do tipo datetime.time")
        self.__horaFim = value

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("O valor deve ser um número")
        if value < 0:
            raise ValueError("O valor não pode ser negativo")
        self.__valor = value

