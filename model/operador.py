from model.endereco import Endereco
from model.fazenda import Fazenda
from model.porto import Porto

class Operador:
    def __init__(self, fazenda: Fazenda, porto: Porto) -> None:
        self.__fazenda = fazenda
        self.__porto = porto

    @property
    def fazenda(self) -> Fazenda:
        return self.__fazenda.mostrar_fazenda()

    @fazenda.setter
    def fazenda(self, fazenda: Fazenda) -> None:
        self.__fazenda = fazenda

    @property
    def porto(self) -> Porto:
        return self.__porto

    @porto.setter
    def porto(self, porto: Porto) -> None:
        self.__porto = porto
