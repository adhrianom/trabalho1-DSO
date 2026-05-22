from model.Pagamento import Pagamento
import datetime

class PagamentoPix(Pagamento):
    def __init__(self, cpfPagador: str, data: datetime.date, valorPago: float):
        super().__init__(data, valorPago)
        self.cpfPagador = cpfPagador

    @property
    def cpfPagador(self):
        return self.__cpfPagador
    
    @cpfPagador.setter
    def cpfPagador(self, value):
        if not isinstance(value, str):
            raise ValueError("O CPF do pagador deve ser uma string")
        if len(value) != 11:
            raise ValueError("O CPF do pagador deve conter 11 dígitos")
        self.__cpfPagador = value