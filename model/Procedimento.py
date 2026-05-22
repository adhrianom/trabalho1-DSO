class Procedimento():
    def __init__(self, descricao: str, custo: float):
        self.descricao = descricao
        self.custo = custo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, value):
        if not isinstance(value, str):
            raise ValueError("A descrição do procedimento deve ser uma string.")
        if not value:
            raise ValueError("A descrição do procedimento não pode ser vazia.")
        self.__descricao = value

    @property
    def custo(self):
        return self.__custo
    
    @custo.setter
    def custo(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("O custo do procedimento deve ser um número.")
        if value < 0:
            raise ValueError("O custo do procedimento não pode ser negativo.")
        self.__custo = value