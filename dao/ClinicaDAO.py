from dao.BaseDAO import BaseDAO


class ClinicaDAO(BaseDAO):
    def __init__(self):
        super().__init__("clinicas.pkl")