from model.Pagamento import Pagamento
import datetime

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: datetime.date, valorPago: float):
        super().__init__(data, valorPago)
