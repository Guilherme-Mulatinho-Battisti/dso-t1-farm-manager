class Cultura:
    """
    Classe que representa uma cultura agrícola.
    - nome: Nome da cultura.
    - dose_semente: Quantidade de semente necessária para a cultura em kg/ha.
    - dose_fertilizante: Dose de fertilizante necessária para a cultura em kg/ha.
    - dose_defensivo: DIct com Dose de defensivo por categoria necessária para a cultura em l/ha.
    - temp_crescimento: Tempo de crescimento da cultura em meses.
    - num_aplicacao: Numero de aplicacoes de defensivo e fertilizante durante o ciclo da cultura.
    """
    def __init__(self, nome: str, id: int, dose_semente: float, dose_fertilizante: float,
                 dose_defensivo: float, temp_crescimento: int, num_aplicacao: int) -> None:
        self.__nome = nome
        self.__id = id
        self.__dose_semente = dose_semente
        self.__dose_fertilizante = dose_fertilizante
        self.__dose_defensivo = dose_defensivo
        self.__temp_crescimento = temp_crescimento
        self.__num_aplicacao = num_aplicacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def dose_semente(self):
        return self.__dose_semente

    @dose_semente.setter
    def dose_semente(self, dose_semente: float) -> None:
        self.__dose_semente = dose_semente

    @property
    def dose_fertilizante(self):
        return self.__dose_fertilizante

    @dose_fertilizante.setter
    def dose_fertilizante(self, dose_fertilizante: float) -> None:
        self.__dose_fertilizante = dose_fertilizante

    @property
    def dose_defensivo(self):
        return self.__dose_defensivo

    @dose_defensivo.setter
    def dose_defensivo(self, dose_defensivo: float) -> None:
        self.__dose_defensivo = dose_defensivo

    @property
    def temp_crescimento(self):
        return self.__temp_crescimento

    @temp_crescimento.setter
    def temp_crescimento(self, temp_crescimento: int) -> None:
        self.__temp_crescimento = temp_crescimento

    @property
    def num_aplicacao(self):
        return self.__num_aplicacao

    @num_aplicacao.setter
    def num_aplicacao(self, num_aplicacao: int) -> None:
        self.__num_aplicacao = num_aplicacao
