import datetime
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, data: datetime.date, valorPago: float):
        super().__init__()
        self.data = data
        self.valorPago = valorPago

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("A data deve ser do tipo datetime.date")
        self.__data = value 

    @property
    def valorPago(self):
        return self.__valorPago

    @valorPago.setter
    def valorPago(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("O valor pago deve ser um número")
        if value < 0:
            raise ValueError("O valor pago não pode ser negativo")
        self.__valorPago = value