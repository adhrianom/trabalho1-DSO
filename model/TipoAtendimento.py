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
        if len(value.strip()) == 0:
            raise ValueError("A descrição do tipo de atendimento não pode ser vazia")
        self.__descricao = value