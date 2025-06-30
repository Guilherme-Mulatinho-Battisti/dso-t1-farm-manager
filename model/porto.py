from model.endereco import Endereco
from model.estoque import Estoque


class Porto:
    def __init__(self, pais: str, estado: str, cidade: str, nome: str, estoque: Estoque) -> None:
        self.__endereco = Endereco(pais, estado, cidade)
        self.__nome = nome
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
    def estoque(self) -> Estoque:
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque: Estoque) -> None:
        self.__estoque = estoque

    def alterar_endereco(self, pais: str, estado: str, cidade: str) -> None:
        """Método para alterar o endereço do porto"""
        self.__endereco = Endereco(pais, estado, cidade)
