from model.Pagamento import Pagamento
import datetime

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numeroCartao: str, bandeira: str, data: datetime.date, valorPago: float):
        super().__init__(data, valorPago)
        self.numeroCartao = numeroCartao 
        self.bandeira = bandeira
    
    @property
    def numeroCartao(self): 
        return self.__numeroCartao
    
    @numeroCartao.setter
    def numeroCartao(self, value):
        if not isinstance(value, str):
            raise ValueError("O número do cartão deve ser uma string")
        if len(value) != 16:
            raise ValueError("O número do cartão deve conter 16 dígitos")
        self.__numeroCartao = value
    
    @property
    def bandeira(self):
        return self.__bandeira
    
    @bandeira.setter
    def bandeira(self, value):
        if not isinstance(value, str):
            raise ValueError("A bandeira do cartão deve ser uma string")
        self.__bandeira = value