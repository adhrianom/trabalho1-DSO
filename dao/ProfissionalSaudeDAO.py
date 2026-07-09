from dao.BaseDAO import BaseDAO


class ProfissionalSaudeDAO(BaseDAO):
    def __init__(self):
        super().__init__("profissionais.pkl")