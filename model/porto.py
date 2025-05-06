from model.endereco import Endereco

class Porto:
    def __init__(self, pais: str, estado: str, cidade: str, nome: str, produtos_disponiveis: list) -> None:
        self.__endereco = Endereco(pais, estado, cidade)
        self.__nome = nome
        self.__produtos_disponiveis = produtos_disponiveis

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
    def produtos_disponiveis(self) -> list:
        return self.__produtos_disponiveis

    @produtos_disponiveis.setter
    def produtos_disponiveis(self, produtos_disponiveis: list) -> None:
        self.__produtos_disponiveis = produtos_disponiveis
