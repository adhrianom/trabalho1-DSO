import datetime

class Atendimento:
    def __init__(self, data: datetime.date, horaInicio: datetime.time, horaFim: datetime.time, valor: float):
        self.data = data
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.valor = valor

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
        self.__valor = value

