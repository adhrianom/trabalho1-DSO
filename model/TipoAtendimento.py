class TipoAtendimento:
    def __init__(self, descricao: str):
        self.descricao = descricao

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, value):
        if not isinstance(value, str):
            raise ValueError("A descrição do tipo de atendimento deve ser uma string")
        self.__descricao = value