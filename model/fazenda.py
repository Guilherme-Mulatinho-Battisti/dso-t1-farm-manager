from model.endereco import Endereco
from model.cultura import Cultura

class Fazenda:
    """ Classe que representa uma fazenda.
        - pais: Pais da fazenda.
        - estado: Estado da fazenda.
        - cidade: Cidade da fazenda.
        - nome: Nome da fazenda.
        - area_plantada: Area de planttacao da fazenda
    """

    def __init__(self, pais: str, estado: str, cidade: str, nome: str, cultura: Cultura, area_plantada: list) -> None:
        self.__endereco = Endereco(pais, estado, cidade)
        self.__nome = nome
        self.__cultura = cultura
        self.__area_plantada = area_plantada

    @property
    def endereco(self) -> str:
        return self.__endereco.mostrar_endereco()

    @endereco.setter
    def endereco(self, pais: str, estado: str, cidade: str) -> None:
        self.__endereco = Endereco(pais, estado, cidade)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def cultura(self) -> str:
        return self.__cultura

    @cultura.setter
    def cultura(self, cultura: str) -> None:
        self.__cultura = cultura

    @property
    def area_plantada(self) -> str:
        return self.__area_plantada

    @area_plantada.setter
    def area_plantada(self, area_plantada: int) -> None:
        self.__area_plantada = area_plantada
