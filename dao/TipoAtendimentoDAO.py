from dao.BaseDAO import BaseDAO


class TipoAtendimentoDAO(BaseDAO):
    def __init__(self):
        super().__init__("tipos_atendimento.pkl")