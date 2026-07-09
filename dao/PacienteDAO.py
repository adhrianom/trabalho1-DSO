from dao.BaseDAO import BaseDAO


class PacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__("pacientes.pkl")