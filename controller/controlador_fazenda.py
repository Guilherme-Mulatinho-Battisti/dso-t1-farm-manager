from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda
from model.estoque import Estoque

class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas = []
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_id(self):
        while True:
            try:
                id_fazenda = int(self.__tela_fazenda.seleciona_fazenda())
                break
            except ValueError:
                self.__tela_fazenda.mostra_mensagem("ID inválido. Digite um número inteiro.")

        for fazenda in self.__fazendas:
            if fazenda.id == id_fazenda:
                return fazenda
        return None

    def incluir_fazenda(self):
        dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
        for fazenda in self.__fazendas:
            if fazenda.id == dados_fazenda["id"]:
                self.__tela_fazenda.mostra_mensagem("ATENÇÃO: Fazenda com esse ID já existe.")
                return

        self.__tela_fazenda.mostra_mensagem("SELECIONE UMA CULTURA ABAIXO DIGITANDO O ID:")
        self.__controlador_sistema.controlador_cultura.listar_culturas()
        cultura_selecionada = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()

        estoque = Estoque(dados_fazenda["id"], {})

        # Adiciona produtos ao estoque durante a criação
        self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(estoque)

        nova_fazenda = Fazenda(
            dados_fazenda["pais"], dados_fazenda["estado"], dados_fazenda["cidade"],
            dados_fazenda["nome"], dados_fazenda["id"],
            cultura_selecionada, dados_fazenda["area_plantada"],
            estoque
        )

        self.__fazendas.append(nova_fazenda)
        self.__tela_fazenda.mostra_mensagem("Fazenda criada com sucesso!")

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
        list_fazenda = self.lista_fazendas()
        if list_fazenda is None:
            return

        fazenda = self.pega_fazenda_por_id()

        if fazenda is not None:
            novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()

            fazenda.nome = novos_dados_fazenda["nome"]
            fazenda.id = novos_dados_fazenda["id"]
            fazenda.pais = novos_dados_fazenda["pais"]
            fazenda.estado = novos_dados_fazenda["estado"]
            fazenda.cidade = novos_dados_fazenda["cidade"]
            fazenda.area_plantada = novos_dados_fazenda["area_plantada"]

            # Alterar cultura
            self.__tela_fazenda.mostra_mensagem("SELECIONE UMA NOVA CULTURA DIGITANDO O ID:")
            self.__controlador_sistema.controlador_cultura.listar_culturas()
            nova_cultura = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()
            if nova_cultura:
                fazenda.cultura = nova_cultura
            else:
                self.__tela_fazenda.mostra_mensagem("Cultura não encontrada. Mantendo a atual.")

            # Alterar estoque
            self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(fazenda.estoque)

            self.__tela_fazenda.mostra_mensagem("Fazenda alterada com sucesso!")
            self.lista_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def lista_fazendas(self):
        if len(self.__fazendas) == 0:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: lista de fazendas vazia")
            return

        for fazenda in self.__fazendas:
            self.__tela_fazenda.mostra_fazenda({"nome": fazenda.nome, "id": fazenda.id,
                                                'endereco': fazenda.endereco,
                                                "cultura": fazenda.cultura.nome,
                                                "area_plantada": fazenda.area_plantada,
                                                "estoque": fazenda.estoque.estoque})
        return self.__fazendas

    def excluir_fazenda(self):
        list_fazenda = self.lista_fazendas()
        if list_fazenda is None:
            return
        fazenda = self.pega_fazenda_por_id()

        if (fazenda is not None):
            self.__fazendas.remove(fazenda)
            self.lista_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def gerenciar_fazenda(self):
        list_fazenda = self.lista_fazendas()
        if list_fazenda is None:
            return
        fazenda = self.pega_fazenda_por_id()

        if fazenda is not None:
            continua = True
            while continua:
                opcao = self.__tela_fazenda.tela_gerenciador_fazenda()
                # Gerenciar estoque
                if opcao == 1:
                    self.__controlador_sistema.controlador_estoque.abre_tela(fazenda.estoque)
                # Alterar cultura
                elif opcao == 2:
                    self.__tela_fazenda.mostra_mensagem("SELECIONE UMA NOVA CULTURA DIGITANDO O ID:")
                    self.__controlador_sistema.controlador_cultura.listar_culturas()
                    nova_cultura = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()
                    if nova_cultura:
                        fazenda.cultura = nova_cultura
                        self.__tela_fazenda.mostra_mensagem("Cultura alterada com sucesso!")
                    else:
                        self.__tela_fazenda.mostra_mensagem("Cultura não encontrada.")
                #  Plantar
                elif opcao == 3:
                    self.__controlador_sistema.controlador_operador.plantar()
                # colher
                elif opcao == 4:
                    self.__controlador_sistema.controlador_operador.colher()
                # aplicar insumo
                elif opcao == 5:
                    self.__controlador_sistema.controlador_operador.aplicar_insumo()
                # retornar
                elif opcao == 0:
                    continua = False
                else:
                    self.__tela_fazenda.mostra_mensagem("Opção inválida.")
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fazenda, 2: self.gerenciar_fazenda,
                        3: self.alterar_fazenda, 4: self.lista_fazendas,
                        5: self.excluir_fazenda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fazenda.tela_opcoes()]()
