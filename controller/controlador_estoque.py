from view.tela_cultura import TelaCultura
from model.cultura import Cultura

class ControladorCultura():

    def __init__(self, controlador_sistema):
        self.__culturas = []
        self.__tela_cultura = TelaCultura()
        self.__controlador_sistema = controlador_sistema

    def pega_cultura_por_id(self, id: int):
        for cultura in self.__culturas:
            if (cultura.id == id):
                return cultura
        return None

    def incluir_cultura(self):
        dados_cultura = self.__tela_cultura.pega_dados_cultura()
        for cultura in self.__culturas:
            if cultura.id == dados_cultura["id"]:
                self.__tela_cultura.mostra_mensagem("ATENÇÃO: Cultura com esse ID já existe.")
                return

        nova_cultura = Cultura(
            dados_cultura["nome"], dados_cultura["id"], dados_cultura["dose_semente"],
            dados_cultura["dose_fertilizante"], dados_cultura["dose_defensivo"],
            dados_cultura["temp_crescimento"], dados_cultura["num_aplicacao"]
        )
        self.__culturas.append(nova_cultura)

    def alterar_cultura(self):
        self.lista_culturas()
        id_cultura = self.__tela_cultura.seleciona_cultura()
        cultura = self.pega_cultura_por_id(id_cultura)

        if (cultura is not None):
            novos_dados_cultura = self.__tela_cultura.pega_dados_cultura()
            cultura.nome = novos_dados_cultura["nome"]
            cultura.telefone = novos_dados_cultura["telefone"]
            cultura.id = novos_dados_cultura["id"]
            self.lista_culturas()
        else:
            self.__tela_cultura.mostra_mensagem("ATENCAO: cultura não existente")

    def lista_culturas(self):
        if len(self.__culturas) == 0:
            self.__tela_cultura.mostra_mensagem("ATENCAO: lista de culturas vazia")
            return

        for cultura in self.__culturas:
            self.__tela_cultura.mostra_cultura({"nome": cultura.nome, "id": cultura.id,
                                                "dose_semente": cultura.dose_semente,
                                                "dose_fertilizante": cultura.dose_fertilizante,
                                                "dose_defensivo": cultura.dose_defensivo,
                                                "temp_crescimento": cultura.temp_crescimento,
                                                "num_aplicacao": cultura.num_aplicacao})

    def excluir_cultura(self):
        self.lista_culturas()
        id_cultura = self.__tela_cultura.seleciona_cultura()
        cultura = self.pega_cultura_por_id(id_cultura)

        if (cultura is not None):
            self.__culturas.remove(cultura)
            self.lista_culturas()
        else:
            self.__tela_cultura.mostra_mensagem("ATENCAO: cultura não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cultura, 2: self.alterar_cultura,
                        3: self.lista_culturas, 4: self.excluir_cultura,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cultura.tela_opcoes()]()
