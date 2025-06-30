from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda
from model.estoque import Estoque


class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas = []
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_id(self, id_fazenda):
        for fazenda in self.__fazendas:
            if fazenda.id == id_fazenda:
                return fazenda
        return None

    def incluir_fazenda(self):
        dados_fazenda = self.__tela_fazenda.pega_dados_fazenda_gui()

        if not dados_fazenda:
            return

        for fazenda in self.__fazendas:
            if fazenda.id == dados_fazenda["id"]:
                self.__tela_fazenda.mostra_mensagem_gui("ATENÇÃO: Fazenda com esse ID já existe.")
                return

        self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA CULTURA NA LISTA:")

        culturas = [
            {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
             "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
             "num_aplicacao": c.num_aplicacao}
            for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
        ]

        id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
        cultura_selecionada = next(
            (c for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all() if
             c.id == id_cultura), None)
        if not cultura_selecionada:
            self.__tela_fazenda.mostra_mensagem_gui("Cultura não selecionada!")
            return
        estoque = Estoque(dados_fazenda["id"], {})
        self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(estoque)
        nova_fazenda = Fazenda(
            dados_fazenda["pais"], dados_fazenda["estado"], dados_fazenda["cidade"],
            dados_fazenda["nome"], dados_fazenda["id"],
            cultura_selecionada, dados_fazenda["area_plantada"],
            estoque
        )
        self.__fazendas.append(nova_fazenda)
        self.__tela_fazenda.mostra_mensagem_gui("Fazenda criada com sucesso!")

    def alterar_cultura(self):
        self.__tela_fazenda.mostra_mensagem("SELECIONE UMA CULTURA ABAIXO DIGITANDO O ID:")
        self.__controlador_sistema.controlador_cultura.listar_culturas()
        cultura_selecionada = self.__controlador_sistema.controlador_cultura.pega_cultura_por_id()

        dados_fazendas = self._dados_saida_fazenda()

        if cultura_selecionada is not None:
            fazenda = self.pega_fazenda_por_id(dados_fazendas)
            fazenda.cultura = cultura_selecionada
            self.__tela_fazenda.mostra_mensagem("Cultura alterada com sucesso!")
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: cultura não existente")

    def alterar_fazenda(self):
        dados = self._dados_saida_fazenda()

        fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(dados)

        if fazenda_id is None:
            self.__tela_fazenda.mostra_mensagem_gui("Nenhuma fazenda selecionada.")
            return

        fazenda = self.pega_fazenda_por_id(fazenda_id)

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
            self.__tela_fazenda.mostra_fazenda_gui(dados)
        else:
            self.__tela_fazenda.mostra_mensagem("ATENCAO: fazenda não existente")

    def listar_fazendas(self):
        if not self.__fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return
        dados = self._dados_saida_fazenda()

        self.__tela_fazenda.mostra_fazenda_gui(dados)

    def alterar_fazenda_gui(self):
        if not self.__fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return

        dados = self._dados_saida_fazenda()

        id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
        fazenda = next((f for f in self.__fazendas if f.id == id_fazenda), None)
        if fazenda is not None:
            novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda_gui()
            if not novos_dados_fazenda:
                return
            fazenda.nome = novos_dados_fazenda["nome"]
            fazenda.id = novos_dados_fazenda["id"]
            fazenda.pais = novos_dados_fazenda["pais"]
            fazenda.estado = novos_dados_fazenda["estado"]
            fazenda.cidade = novos_dados_fazenda["cidade"]
            fazenda.area_plantada = novos_dados_fazenda["area_plantada"]
            # Alterar cultura
            self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA NA LISTA:")
            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                 "num_aplicacao": c.num_aplicacao}
                for c in self.__controlador_sistema.controlador_cultura._ControladorCultura__culturas_DAO.get_all()
            ]
            id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
            nova_cultura = next(
                (c for c in self.__controlador_sistema.controlador_cultura._ControladorCultura__culturas_DAO.get_all()
                 if c.id == id_cultura), None)
            if nova_cultura:
                fazenda.cultura = nova_cultura
            else:
                self.__tela_fazenda.mostra_mensagem_gui("Cultura não encontrada. Mantendo a atual.")
            # Alterar estoque
            self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(fazenda.estoque)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda alterada com sucesso!")
            self.listar_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: fazenda não existente")

    def excluir_fazenda_gui(self):
        if not self.__fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return

        dados = self._dados_saida_fazenda()

        id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
        fazenda = next((f for f in self.__fazendas if f.id == id_fazenda), None)
        if fazenda is not None:
            self.__fazendas.remove(fazenda)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda excluída com sucesso!")
            self.listar_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: fazenda não existente")

    def gerenciar_fazenda(self):
        fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(self.__fazendas)

        fazenda = self.pega_fazenda_por_id(fazenda_id)

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
                # aplicar defensivo
                elif opcao == 5:
                    self.__controlador_sistema.controlador_operador.aplicar_defensivo()
                # aplicar fertilizante
                elif opcao == 6:
                    self.__controlador_sistema.controlador_operador.aplicar_fertilizante()
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
                        3: self.alterar_fazenda_gui, 4: self.listar_fazendas,
                        5: self.excluir_fazenda_gui, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fazenda.tela_opcoes_gui()]()

    def _dados_saida_fazenda(self):
        dados = []
        for fazenda in self.__fazendas:
            dados.append({
                "nome": fazenda.nome,
                "id": fazenda.id,
                "pais": fazenda.pais,
                "estado": fazenda.estado,
                "cidade": fazenda.cidade,
                "cultura": fazenda.cultura.nome if fazenda.cultura else "",
                "area_plantada": fazenda.area_plantada,
                "estoque": fazenda.estoque.estoque if fazenda.estoque else ""
            })
        return dados
