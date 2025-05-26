from model.endereco import Endereco
from model.cultura import Cultura
from model.estoque import Estoque

class Fazenda:
    """ Classe que representa uma fazenda.
        - pais: Pais da fazenda.
        - estado: Estado da fazenda.
        - cidade: Cidade da fazenda.
        - nome: Nome da fazenda.
        - area_plantada: Area de planttacao da fazenda
    """

    def __init__(self, pais: str, estado: str, cidade: str, nome: str, id: int,
                 cultura: Cultura, area_plantada: int, estoque: Estoque) -> None:
        self.__endereco = Endereco(pais, estado, cidade)
        self.__nome = nome
        self.__id = id
        self.__cultura = cultura
        self.__area_plantada = area_plantada
        self.__estoque = estoque

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
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def cultura(self) -> Cultura:
        return self.__cultura

    @cultura.setter
    def cultura(self, cultura: Cultura) -> None:
        self.__cultura = cultura

    @property
    def area_plantada(self) -> str:
        return self.__area_plantada

    @area_plantada.setter
    def area_plantada(self, area_plantada: int) -> None:
        self.__area_plantada = area_plantada

    @property
    def estoque(self) -> Estoque:
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque: Estoque) -> None:
        self.__estoque = estoque
