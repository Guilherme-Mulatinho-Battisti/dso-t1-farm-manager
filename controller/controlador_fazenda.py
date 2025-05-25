from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda

class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas = []
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_endereco(self, endereco: int):
        for fazenda in self.__fazendas:
            if (fazenda.id == id):
                return fazenda
        return None

    def incluir_fazenda(self):
        dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
        for fazenda in self.__fazendas:
            if fazenda.id == dados_fazenda["id"]:
                self.__tela_fazenda.mostra_mensagem("ATENÇÃO: Fazenda com esse ID já existe.")
                return

        nova_fazenda = Fazenda(
            dados_fazenda["nome"], dados_fazenda["id"], dados_fazenda["dose_semente"],
            dados_fazenda["dose_fertilizante"], dados_fazenda["dose_defensivo"],
            dados_fazenda["temp_crescimento"], dados_fazenda["num_aplicacao"]
        )
        self.__fazendas.append(nova_fazenda)

    def alterar_fazenda(self):
        self.lista_fazendas()
        id_fazenda = self.__tela_fazenda.seleciona_fazenda()
        fazenda = self.pega_fazenda_por_id(id_fazenda)

        if (fazenda is not None):
            novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
            fazenda.nome = novos_dados_fazenda["nome"]
            fazenda.telefone = novos_dados_fazenda["telefone"]
            fazenda.id = novos_dados_fazenda["id"]
            self.lista_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def lista_fazendas(self):
        if len(self.__fazendas) == 0:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: lista de fazendas vazia")
            return

        for fazenda in self.__fazendas:
            self.__tela_fazenda.mostra_fazenda({"nome": fazenda.nome, "id": fazenda.id,
                                                "dose_semente": fazenda.dose_semente,
                                                "dose_fertilizante": fazenda.dose_fertilizante,
                                                "dose_defensivo": fazenda.dose_defensivo,
                                                "temp_crescimento": fazenda.temp_crescimento,
                                                "num_aplicacao": fazenda.num_aplicacao})

    def excluir_fazenda(self):
        self.lista_fazendas()
        id_fazenda = self.__tela_fazenda.seleciona_fazenda()
        fazenda = self.pega_fazenda_por_id(id_fazenda)

        if (fazenda is not None):
            self.__fazendas.remove(fazenda)
            self.lista_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def gerenciar_fazenda(self):

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fazenda, 2: self.alterar_fazenda,
                        3: self.lista_fazendas, 4: self.excluir_fazenda,
                        5: self.gerenciar_fazenda,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fazenda.tela_opcoes()]()
