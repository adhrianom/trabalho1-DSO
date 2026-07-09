from dao.BaseDAO import BaseDAO


class PagamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__("pagamentos.pkl")