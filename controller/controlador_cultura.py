from view.tela_cultura import TelaCultura
from model.cultura import Cultura
from DAOs.dao_cultura import CulturaDAO


class ControladorCultura():

    def __init__(self, controlador_sistema):
        # self.__culturas = []
        self.__culturas_DAO = CulturaDAO()

        self.__controlador_sistema = controlador_sistema
        self.__tela_cultura = TelaCultura()
        # self.carrega_dados()

    # def carrega_dados(self):
    #     """ Método para carregar dados de culturas pré-definidas. """
    #     self.__culturas.append(Cultura(nome='Soja', id=1, dose_semente=0.8, dose_fertilizante=40,
    #                                    dose_defensivo=30, temp_crescimento=8, num_aplicacao=1))
    #     self.__culturas.append(Cultura(nome='Milho', id=2, dose_semente=2, dose_fertilizante=30,
    #                                    dose_defensivo=50, temp_crescimento=10, num_aplicacao=2))
    #     self.__culturas.append(Cultura(nome='Trigo', id=3, dose_semente=0.5, dose_fertilizante=22,
    #                                    dose_defensivo=34, temp_crescimento=8, num_aplicacao=1))
    #     self.__culturas.append(Cultura(nome='Algodao', id=4, dose_semente=1.2, dose_fertilizante=60,
    #                                    dose_defensivo=36, temp_crescimento=8, num_aplicacao=1))

    def pega_cultura_por_id(self):
        while True:
            try:
                id_cultura = int(self.__tela_cultura.seleciona_cultura_gui(self.__culturas_DAO.get_all()))
                break
            except ValueError:
                self.__tela_cultura.mostra_mensagem("ID inválido. Digite um número inteiro.")

        for cultura in self.__culturas_DAO.get_all():
            if cultura.id == id_cultura:
                return cultura
        return None

    def incluir_cultura(self):
        dados_cultura = self.__tela_cultura.pega_dados_cultura()
        for cultura in self.__culturas_DAO.get_all():
            if cultura.id == dados_cultura["id"]:
                self.__tela_cultura.mostra_mensagem("ATENÇÃO: Cultura com esse ID já existe.")
                return

        nova_cultura = Cultura(
            dados_cultura["nome"], dados_cultura["id"], dados_cultura["dose_semente"],
            dados_cultura["dose_fertilizante"], dados_cultura["dose_defensivo"],
            dados_cultura["temp_crescimento"], dados_cultura["num_aplicacao"]
        )
        self.__culturas_DAO.add(nova_cultura)

    def incluir_cultura_gui(self):
        dados_cultura = self.__tela_cultura.pega_dados_cultura_gui()
        if not dados_cultura:
            return
        for cultura in self.__culturas_DAO.get_all():
            if cultura.id == dados_cultura["id"]:
                self.__tela_cultura.mostra_mensagem_gui("ATENÇÃO: Cultura com esse ID já existe.")
                return
        nova_cultura = Cultura(
            dados_cultura["nome"], dados_cultura["id"], dados_cultura["dose_semente"],
            dados_cultura["dose_fertilizante"], dados_cultura["dose_defensivo"],
            dados_cultura["temp_crescimento"], dados_cultura["num_aplicacao"]
        )
        self.__culturas_DAO.add(nova_cultura)
        self.__tela_cultura.mostra_mensagem_gui("Cultura adicionada com sucesso!")

    def alterar_cultura(self):
        self.listar_culturas()
        cultura = self.pega_cultura_por_id()

        if (cultura is not None):
            novos_dados_cultura = self.__tela_cultura.pega_dados_cultura()
            cultura.nome = novos_dados_cultura["nome"]
            cultura.id = novos_dados_cultura["id"]
            cultura.dose_semente = novos_dados_cultura["dose_semente"]
            cultura.dose_fertilizante = novos_dados_cultura["dose_fertilizante"]
            cultura.dose_defensivo = novos_dados_cultura["dose_defensivo"]
            cultura.temp_crescimento = novos_dados_cultura["temp_crescimento"]
            cultura.num_aplicacao = novos_dados_cultura["num_aplicacao"]
            self.listar_culturas()
        else:
            self.__tela_cultura.mostra_mensagem("ATENCAO: cultura não existente")

    def listar_culturas(self):
        culturas = self.__culturas_DAO.get_all()
        if len(culturas) == 0:
            self.__tela_cultura.mostra_mensagem("ATENCAO: lista de culturas vazia")
            return

        dados_saida = []
        for cultura in culturas:
            dados_saida.append({"nome": cultura.nome, "id": cultura.id,
                                                "dose_semente": cultura.dose_semente,
                                                "dose_fertilizante": cultura.dose_fertilizante,
                                                "dose_defensivo": cultura.dose_defensivo,
                                                "temp_crescimento": cultura.temp_crescimento,
                                                "num_aplicacao": cultura.num_aplicacao})

        self.__tela_cultura.mostra_culturas_gui(dados_saida)

    def listar_culturas_gui(self):
        culturas = [
            {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
             "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
            for c in self.__culturas_DAO.get_all()
        ]
        self.__tela_cultura.mostra_culturas_gui(culturas)

    def alterar_cultura_gui(self):
        culturas = [
            {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
             "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
            for c in self.__culturas_DAO.get_all()
        ]
        id_cultura = self.__tela_cultura.seleciona_cultura_gui(culturas)
        if id_cultura is None:
            return
        cultura = next((c for c in self.__culturas_DAO.get_all() if c.id == id_cultura), None)
        if cultura is not None:
            novos_dados_cultura = self.__tela_cultura.pega_dados_cultura_gui()
            if not novos_dados_cultura:
                return
            cultura.nome = novos_dados_cultura["nome"]
            cultura.id = novos_dados_cultura["id"]
            cultura.dose_semente = novos_dados_cultura["dose_semente"]
            cultura.dose_fertilizante = novos_dados_cultura["dose_fertilizante"]
            cultura.dose_defensivo = novos_dados_cultura["dose_defensivo"]
            cultura.temp_crescimento = novos_dados_cultura["temp_crescimento"]
            cultura.num_aplicacao = novos_dados_cultura["num_aplicacao"]
            self.__tela_cultura.mostra_mensagem_gui("Cultura alterada com sucesso!")
            self.listar_culturas_gui()
        else:
            self.__tela_cultura.mostra_mensagem_gui("ATENCAO: cultura não existente")

    def excluir_cultura(self):
        self.listar_culturas()
        cultura = self.pega_cultura_por_id()

        if (cultura is not None):
            self.__culturas_DAO.remove(cultura)
            self.listar_culturas()
        else:
            self.__tela_cultura.mostra_mensagem("ATENCAO: cultura não existente")

    def excluir_cultura_gui(self):
        culturas = [
            {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
             "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
            for c in self.__culturas_DAO.get_all()
        ]
        id_cultura = self.__tela_cultura.seleciona_cultura_gui(culturas)
        if id_cultura is None:
            return
        cultura = next((c for c in self.__culturas_DAO.get_all() if c.id == id_cultura), None)
        if cultura is not None:
            self.__culturas_DAO.remove(cultura)
            self.__tela_cultura.mostra_mensagem_gui("Cultura excluída com sucesso!")
            self.listar_culturas_gui()
        else:
            self.__tela_cultura.mostra_mensagem_gui("ATENCAO: cultura não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cultura_gui,
                        2: self.alterar_cultura_gui,
                        3: self.listar_culturas_gui,
                        4: self.excluir_cultura_gui,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cultura.tela_opcoes_gui()]()
