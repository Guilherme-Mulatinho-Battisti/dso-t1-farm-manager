from view.tela_porto import TelaPorto
from model.porto import Porto
from model.estoque import Estoque

class ControladorPorto():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__porto = Porto("Brasil", "SP", "Sao Paulo", "Porto Central", Estoque(0, {}))
        self.__tela_porto = TelaPorto()
        self.carrega_dados()

    def carrega_dados(self, quantidade_padrao=100):
        insumos = self.__controlador_sistema.controlador_insumo.insumos
        for insumo in insumos:
            self.__porto.estoque.estoque[insumo.nome] = quantidade_padrao
            self.__controlador_sistema.controlador_estoque.registrar_log(
                self.__porto.estoque, "ADICIONADO", insumo.nome, quantidade_padrao
            )

    def incluir_porto(self):
        dados_porto = self.__tela_porto.pega_dados_porto()
        for porto in self.__portos:
            if porto.id == dados_porto["id"]:
                self.__tela_porto.mostra_mensagem("ATENÇÃO: Porto com esse ID já existe.")
                return

        self.__tela_porto.mostra_mensagem("SELECIONE UMA CULTURA ABAIXO DIGITANDO O ID:")
        self.__controlador_sistema.controlador_cultura.listar_culturas()
        cultura_selecionada = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()

        estoque = Estoque(dados_porto["id"], {})

        # Adiciona produtos ao estoque durante a criação
        self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(estoque)

        nova_porto = Porto(
            dados_porto["pais"], dados_porto["estado"], dados_porto["cidade"],
            dados_porto["nome"], dados_porto["id"],
            cultura_selecionada, dados_porto["area_plantada"],
            estoque
        )

        self.__portos.append(nova_porto)
        self.__tela_porto.mostra_mensagem("Porto criada com sucesso!")

    def alterar_porto(self):
        list_porto = self.lista_portos()
        if list_porto is None:
            return

        porto = self.pega_porto_por_id()

        if porto is not None:
            novos_dados_porto = self.__tela_porto.pega_dados_porto()

            porto.nome = novos_dados_porto["nome"]
            porto.id = novos_dados_porto["id"]
            porto.pais = novos_dados_porto["pais"]
            porto.estado = novos_dados_porto["estado"]
            porto.cidade = novos_dados_porto["cidade"]

            # Alterar cultura
            self.__tela_porto.mostra_mensagem("SELECIONE UMA NOVA CULTURA DIGITANDO O ID:")
            self.__controlador_sistema.controlador_cultura.listar_culturas()
            nova_cultura = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()
            if nova_cultura:
                porto.cultura = nova_cultura
            else:
                self.__tela_porto.mostra_mensagem("Cultura não encontrada. Mantendo a atual.")

            # Alterar estoque
            self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(porto.estoque)

            self.__tela_porto.mostra_mensagem("Porto alterada com sucesso!")
            self.lista_portos()
        else:
            self.__tela_porto.mostra_mensagem("ATENCAO: porto não existente")

    def lista_portos(self):
        if len(self.__portos) == 0:
            self.__tela_porto.mostra_mensagem("ATENCAO: lista de portos vazia")
            return

        for porto in self.__portos:
            self.__tela_porto.mostra_porto({"nome": porto.nome, "id": porto.id,
                                                'endereco': porto.endereco,
                                                "cultura": porto.cultura.nome,
                                                "area_plantada": porto.area_plantada,
                                                "estoque": porto.estoque.estoque})
        return self.__portos

    def excluir_porto(self):
        list_porto = self.lista_portos()
        if list_porto is None:
            return
        porto = self.pega_porto_por_id()

        if (porto is not None):
            self.__portos.remove(porto)
            self.lista_portos()
        else:
            self.__tela_porto.mostra_mensagem("ATENCAO: porto não existente")

    def gerenciar_porto(self):
        list_porto = self.lista_portos()
        if list_porto is None:
            return
        porto = self.pega_porto_por_id()

        if porto is not None:
            continua = True
            while continua:
                opcao = self.__tela_porto.tela_gerenciador_porto()
                # Gerenciar estoque
                if opcao == 1:
                    self.__controlador_sistema.controlador_estoque.abre_tela(porto.estoque)
                # Alterar cultura
                elif opcao == 2:
                    self.__tela_porto.mostra_mensagem("SELECIONE UMA NOVA CULTURA DIGITANDO O ID:")
                    self.__controlador_sistema.controlador_cultura.listar_culturas()
                    nova_cultura = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()
                    if nova_cultura:
                        porto.cultura = nova_cultura
                        self.__tela_porto.mostra_mensagem("Cultura alterada com sucesso!")
                    else:
                        self.__tela_porto.mostra_mensagem("Cultura não encontrada.")
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
                    self.__tela_porto.mostra_mensagem("Opção inválida.")
        else:
            self.__tela_porto.mostra_mensagem("ATENCAO: porto não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_porto, 2: self.gerenciar_porto,
                        3: self.alterar_porto, 4: self.lista_portos,
                        5: self.excluir_porto, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_porto.tela_opcoes()]()
