from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda
from model.estoque import Estoque

class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas = []
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_id(self):
        id_fazenda = self.__tela_fazenda.seleciona_fazenda()
        for fazenda in self.__fazendas:
            if (fazenda.id == id_fazenda):
                return fazenda
        return None

    def incluir_fazenda(self):
        dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
        for fazenda in self.__fazendas:
            if fazenda.id == dados_fazenda["id"]:
                self.__tela_fazenda.mostra_mensagem("ATENÇÃO: Fazenda com esse ID já existe.")
                return

        # Parte da Seleção das culturas
        self.__tela_fazenda.mostra_mensagem("SELECIONE UMA CULTURA ABAIXO DIGITANDO O ID:")
        self.__controlador_sistema.controlador_cultura.listar_culturas()
        cultura_selecionada = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()

        # Seleciona Estoque
        self.__tela_fazenda.mostra_mensagem("SELECIONE UM ESTOQUE ABAIXO DIGITANDO O ID:")

        nova_fazenda = Fazenda(
            dados_fazenda["pais"], dados_fazenda["estado"], dados_fazenda["cidade"],
            dados_fazenda["nome"], dados_fazenda["id"],
            cultura_selecionada, dados_fazenda["area_plantada"],
            Estoque(dados_fazenda["id"], {})
        )
        
        self.__fazendas.append(nova_fazenda)

    def alterar_cultura(self):
        self.__tela_fazenda.mostra_mensagem("SELECIONE UMA CULTURA ABAIXO DIGITANDO O ID:")
        self.__controlador_sistema.controlador_cultura.listar_culturas()
        cultura_selecionada = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()

        if cultura_selecionada is not None:
            fazenda = self.pega_fazenda_por_id()
            fazenda.cultura = cultura_selecionada
            self.__tela_fazenda.mostra_mensagem("Cultura alterada com sucesso!")
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: cultura não existente")

    def alterar_fazenda(self):
        self.lista_fazendas()
        fazenda = self.pega_fazenda_por_id()

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
        fazenda = self.pega_fazenda_por_id()

        if (fazenda is not None):
            self.__fazendas.remove(fazenda)
            self.lista_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def gerenciar_fazenda(self):
        self.lista_fazendas()
        fazenda = self.pega_fazenda_por_id()
        if (fazenda is not None):
            lista_opcoes = {1: self.__controlador_sistema.controlador_estoque.gerenciar_estoque,
                            2: self.alterar_cultura(),
                            0: self.retornar}

            continua = True
            while continua:
                lista_opcoes[self.__tela_fazenda.tela_gerenciador_fazenda()]()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

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
