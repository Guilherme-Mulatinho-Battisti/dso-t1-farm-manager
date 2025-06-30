from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda
from model.estoque import Estoque
from DAOs.dao_fazenda import FazendaDAO


class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas_DAO = FazendaDAO()
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_id(self, id_fazenda):
        return self.__fazendas_DAO.get(id_fazenda)

    def incluir_fazenda(self):
        dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()

        if not dados_fazenda:
            return

        # Verificar se já existe fazenda com esse ID
        fazenda_existente = self.__fazendas_DAO.get(dados_fazenda["id"])
        if fazenda_existente:
            self.__tela_fazenda.mostra_mensagem_gui("ATENÇÃO: Fazenda com esse ID já existe.")
            return

        # Verificar se há culturas cadastradas
        culturas_obj = self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
        if not culturas_obj:
            self.__tela_fazenda.mostra_mensagem_gui("ERRO: Não há culturas cadastradas! Cadastre uma cultura primeiro.")
            return

        self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA CULTURA NA LISTA:")

        culturas = [
            {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
             "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
             "num_aplicacao": c.num_aplicacao}
            for c in culturas_obj
        ]

        id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
        
        if id_cultura is None:
            self.__tela_fazenda.mostra_mensagem_gui("Nenhuma cultura selecionada. Operação cancelada.")
            return
            
        cultura_selecionada = next(
            (c for c in culturas_obj if c.id == id_cultura), None)
        
        if not cultura_selecionada:
            self.__tela_fazenda.mostra_mensagem_gui("Erro: Cultura não encontrada!")
            return
            
        estoque = Estoque(dados_fazenda["id"], {})
        nova_fazenda = Fazenda(
            dados_fazenda["pais"], dados_fazenda["estado"], dados_fazenda["cidade"],
            dados_fazenda["nome"], dados_fazenda["id"],
            cultura_selecionada, dados_fazenda["area_plantada"],
            estoque
        )
        self.__fazendas_DAO.add(nova_fazenda)
        self.__tela_fazenda.mostra_mensagem_gui("Fazenda criada com sucesso!")

    def alterar_fazenda(self):
        dados = self._dados_saida_fazenda()

        fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(dados)

        if fazenda_id is None:
            self.__tela_fazenda.mostra_mensagem_gui("Nenhuma fazenda selecionada.")
            return

        fazenda = self.pega_fazenda_por_id(fazenda_id)

        if fazenda is not None:
            novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
            
            if not novos_dados_fazenda:
                self.__tela_fazenda.mostra_mensagem_gui("Alteração cancelada.")
                return

            fazenda.nome = novos_dados_fazenda["nome"]
            fazenda.id = novos_dados_fazenda["id"]
            fazenda.pais = novos_dados_fazenda["pais"]
            fazenda.estado = novos_dados_fazenda["estado"]
            fazenda.cidade = novos_dados_fazenda["cidade"]
            fazenda.area_plantada = novos_dados_fazenda["area_plantada"]

            # Alterar cultura usando GUI
            self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA:")
            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                 "num_aplicacao": c.num_aplicacao}
                for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
            ]
            
            id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
            nova_cultura = next(
                (c for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all() if
                 c.id == id_cultura), None)
            if nova_cultura:
                fazenda.cultura = nova_cultura
            else:
                self.__tela_fazenda.mostra_mensagem_gui("Cultura não encontrada. Mantendo a atual.")

            # Alterar estoque
            self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(fazenda.estoque)

            # Atualizar fazenda no DAO
            self.__fazendas_DAO.update(fazenda)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda alterada com sucesso!")
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENÇÃO: fazenda não existente")

    def listar_fazendas(self):
        fazendas = list(self.__fazendas_DAO.get_all())
        if not fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return
        dados = self._dados_saida_fazenda()

        self.__tela_fazenda.mostra_fazenda_gui(dados)

    def alterar_fazenda_gui(self):
        fazendas = list(self.__fazendas_DAO.get_all())
        if not fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return

        dados = self._dados_saida_fazenda()

        id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
        fazenda = self.pega_fazenda_por_id(id_fazenda)
        if fazenda is not None:
            novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
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
                for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
            ]
            id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
            nova_cultura = next(
                (c for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
                 if c.id == id_cultura), None)
            if nova_cultura:
                fazenda.cultura = nova_cultura
            else:
                self.__tela_fazenda.mostra_mensagem_gui("Cultura não encontrada. Mantendo a atual.")
            # Alterar estoque
            self.__controlador_sistema.controlador_estoque.adicionar_produto_ao_estoque(fazenda.estoque)
            
            # Atualizar fazenda no DAO
            self.__fazendas_DAO.update(fazenda)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda alterada com sucesso!")
            self.listar_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: fazenda não existente")

    def excluir_fazenda_gui(self):
        fazendas = list(self.__fazendas_DAO.get_all())
        if not fazendas:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: lista de fazendas vazia")
            return

        dados = self._dados_saida_fazenda()

        id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
        if id_fazenda is None:
            self.__tela_fazenda.mostra_mensagem_gui("Nenhuma fazenda selecionada.")
            return
            
        fazenda = self.pega_fazenda_por_id(id_fazenda)
        if fazenda is not None:
            self.__fazendas_DAO.remove(id_fazenda)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda excluída com sucesso!")
            self.listar_fazendas()
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: fazenda não existente")

    def gerenciar_fazenda(self):
        dados = self._dados_saida_fazenda()
        fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(dados)

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
                    self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA NA LISTA:")
                    culturas = [
                        {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                         "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                         "num_aplicacao": c.num_aplicacao}
                        for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all()
                    ]
                    id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
                    nova_cultura = next(
                        (c for c in self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all() if
                         c.id == id_cultura), None)
                    if nova_cultura:
                        fazenda.cultura = nova_cultura
                        self.__fazendas_DAO.update(fazenda)  # Persistir a alteração
                        self.__tela_fazenda.mostra_mensagem_gui("Cultura alterada com sucesso!")
                    else:
                        self.__tela_fazenda.mostra_mensagem_gui("Cultura não encontrada.")
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
                    self.__tela_fazenda.mostra_mensagem_gui("Opção inválida.")
        else:
            self.__tela_fazenda.mostra_mensagem_gui("ATENCAO: fazenda não existente")

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
        for fazenda in self.__fazendas_DAO.get_all():
            # Tratamento seguro para estoque
            estoque_info = ""
            if fazenda.estoque and fazenda.estoque.estoque:
                produtos = []
                for produto, qtd in fazenda.estoque.estoque.items():
                    produtos.append(f"{produto}: {qtd}")
                estoque_info = ", ".join(produtos) if produtos else "Vazio"
            else:
                estoque_info = "Vazio"
            
            dados.append({
                "nome": fazenda.nome,
                "id": fazenda.id,
                "pais": fazenda.pais,
                "estado": fazenda.estado,
                "cidade": fazenda.cidade,
                "cultura": fazenda.cultura.nome if fazenda.cultura else "N/A",
                "area_plantada": fazenda.area_plantada,
                "estoque": estoque_info
            })
        return dados
