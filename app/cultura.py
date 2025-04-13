class Cultura:
    """
    Classe que representa uma cultura agrícola.
    - nome: Nome da cultura.
    - quant_semente: Quantidade de semente necessária para a cultura em kg/ha.
    - dose_fertilizante: Dose de fertilizante necessária para a cultura em kg/ha.
    - dose_defensivo: Dose de defensivo necessária para a cultura em l/ha.
    - temp_crescimento: Tempo de crescimento da cultura em meses.
    - num_aplicacao: Numero de aplicacoes de defensivo e fertilizante durante o ciclo da cultura.
    """
    def __init__(self, nome: str, quant_semente: float, dose_fertilizante: float,
                 dose_defensivo: float, temp_crescimento: int, num_aplicacao: int) -> None:
        self.__nome = nome
        self.__quant_semente = quant_semente
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
    def quant_semente(self):
        return self.__quant_semente

    @quant_semente.setter
    def quant_semente(self, quant_semente: float) -> None:
        self.__quant_semente = quant_semente

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
