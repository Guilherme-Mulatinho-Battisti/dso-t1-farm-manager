class Endereco():
    """ Classe que representa um endereço.
        - pais: Pais do endereço.
        - estado: Estado do endereço.
        - cidade: Cidade do endereço.
    """

    def __init__(self, pais: str, estado: str, cidade: str) -> None:
        self.__pais = pais
        self.__estado = estado
        self.__cidade = cidade

    def mostrar_endereco(self) -> str:
        """ Método que retorna o endereço formatado. """
        return f"{self.__pais}, {self.__estado}, {self.__cidade}"
