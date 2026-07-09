from dao.BaseDAO import BaseDAO


class AtendimentoDAO(BaseDAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")