from abc import ABC, abstractmethod

class Insumo(ABC):

    @abstractmethod
    def __init__(self, nome: str, valor: float):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor


class Defensivo(Insumo):
    """ Classe que representa um defensivo(agrotoxico) agrícola.
        - nome: Nome do defensivo.
        - valor: Valor do defensivo por litro.
        - funcao: Função do defensivo (Herbicida, Fungicida, Inseticida ou Acaricida)
    """
    def __init__(self, nome: str, valor: float, funcao: str):
        super().__init__(nome, valor)
        self.__funcao = funcao

    @property
    def funcao(self) -> str:
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao: str) -> None:
        self.__funcao = funcao

class Fertilizante(Insumo):
    """ Classe que representa um fertilizante.
        - nome: Nome do fertilizante.
        - valor: Valor do fertilizante por KG.
        - fonte: Fonte do fertilizante (Organico ou Quimico).
    """
    def __init__(self, nome: str, valor: float, fonte: str):
        super().__init__(nome, valor)
        self.__fonte = fonte

    @property
    def fonte(self) -> str:
        return self.__fonte

    @fonte.setter
    def fonte(self, fonte: str) -> None:
        self.__fonte = fonte

class Implemento(Insumo):
    """ Classe que representa um implemento agrícola.
        - nome: Nome do implemento.
        - valor: Valor do implemento por hequitare.
        - processo: Processo do implemento (Pantio ou Colheita).
        - tipo: Tipo do implemento (Manual ou Mecanico)
    """
    def __init__(self, nome: str, valor: float, processo: str, tipo: str):
        super().__init__(nome, valor)
        self.__processo = processo
        self.__tipo = tipo

    @property
    def processo(self) -> str:
        return self.__processo

    @processo.setter
    def processo(self, processo: str) -> None:
        self.__processo = processo

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self.__tipo = tipo

class Semente(Insumo):
    """ Classe que representa uma semente agrícola.
        - nome: Nome do semente.
        - valor: Valor do semente por KG
        - cultura: Cultura do semente (Soja, Milho, Trigo ou Algodão)
        - tecnologia: Tecnologia do semente (Transgenica ou Nao Transgenica)
    """
    def __init__(self, nome: str, valor: float, cultura: str, tecnologia: str):
        super().__init__(nome, valor)
        self.__cultura = cultura
        self.__tecnologia = tecnologia

    @property
    def cultura(self) -> str:
        return self.__cultura

    @cultura.setter
    def cultura(self, cultura: str) -> None:
        self.__cultura = cultura

    @property
    def tecnologia(self) -> str:
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, tecnologia: str) -> None:
        self.__tecnologia = tecnologia
