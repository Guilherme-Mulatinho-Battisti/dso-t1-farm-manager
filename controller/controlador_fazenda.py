from view.tela_fazenda import TelaFazenda
from model.fazenda import Fazenda
from model.estoque import Estoque
from DAOs.dao_fazenda import FazendaDAO
from exceptions.custom_exception import (
    OpcaoNaoExistenteException, 
    ListaVaziaException, 
    ItemJaExisteException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)


class ControladorFazenda():
    def __init__(self, controlador_sistema):
        self.__fazendas_DAO = FazendaDAO()
        self.__tela_fazenda = TelaFazenda()
        self.__controlador_sistema = controlador_sistema

    def pega_fazenda_por_id(self, id_fazenda):
        try:
            if id_fazenda is None:
                raise DadosInvalidosException("ID da fazenda não pode ser nulo.")
            
            fazenda = self.__fazendas_DAO.get(id_fazenda)
            if fazenda is None:
                raise ItemNaoEncontradoException(f"Fazenda com ID {id_fazenda} não encontrada.")
            
            return fazenda
        except (DadosInvalidosException, ItemNaoEncontradoException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO: {str(e)}")
            return None
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado: {str(e)}")
            return None

    def incluir_fazenda(self):
        try:
            dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()

            if not dados_fazenda:
                raise OperacaoCanceladaException("Cadastro de fazenda cancelado.")

            # Verificar se já existe fazenda com esse ID
            fazenda_existente = self.__fazendas_DAO.get(dados_fazenda["id"])
            if fazenda_existente:
                raise ItemJaExisteException("Fazenda com esse ID já existe.")

            # Verificar se há culturas cadastradas
            culturas_obj = list(self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all())
            if not culturas_obj:
                raise ListaVaziaException("Não há culturas cadastradas! Cadastre uma cultura primeiro.")

            self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA CULTURA NA LISTA:")

            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                 "num_aplicacao": c.num_aplicacao}
                for c in culturas_obj
            ]

            id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
            
            if id_cultura is None:
                raise OperacaoCanceladaException("Nenhuma cultura selecionada.")
                
            cultura_selecionada = next(
                (c for c in culturas_obj if c.id == id_cultura), None)
            
            if not cultura_selecionada:
                raise ItemNaoEncontradoException("Cultura não encontrada!")
                
            estoque = Estoque(dados_fazenda["id"], {})
            nova_fazenda = Fazenda(
                dados_fazenda["pais"], dados_fazenda["estado"], dados_fazenda["cidade"],
                dados_fazenda["nome"], dados_fazenda["id"],
                cultura_selecionada, dados_fazenda["area_plantada"],
                estoque
            )
            self.__fazendas_DAO.add(nova_fazenda)
            self.__tela_fazenda.mostra_mensagem_gui("Fazenda criada com sucesso!")
            
        except (OperacaoCanceladaException, ItemJaExisteException, ListaVaziaException, ItemNaoEncontradoException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao criar fazenda: {str(e)}")

    def alterar_fazenda(self):
        try:
            dados = self._dados_saida_fazenda()

            fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(dados)

            if fazenda_id is None:
                raise OperacaoCanceladaException("Nenhuma fazenda selecionada.")

            fazenda = self.pega_fazenda_por_id(fazenda_id)

            if fazenda is not None:
                novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
                
                if not novos_dados_fazenda:
                    raise OperacaoCanceladaException("Alteração cancelada pelo usuário.")

                fazenda.nome = novos_dados_fazenda["nome"]
                fazenda.id = novos_dados_fazenda["id"]
                fazenda.pais = novos_dados_fazenda["pais"]
                fazenda.estado = novos_dados_fazenda["estado"]
                fazenda.cidade = novos_dados_fazenda["cidade"]
                fazenda.area_plantada = novos_dados_fazenda["area_plantada"]

                # Alterar cultura usando GUI
                self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA:")
                culturas_obj = list(self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all())
                if not culturas_obj:
                    raise ListaVaziaException("Não há culturas cadastradas!")
                
                culturas = [
                    {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                     "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                     "num_aplicacao": c.num_aplicacao}
                    for c in culturas_obj
                ]
                
                id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
                nova_cultura = next(
                    (c for c in culturas_obj if
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
                raise ItemNaoEncontradoException("Fazenda não encontrada")
                
        except (OperacaoCanceladaException, ItemNaoEncontradoException, ListaVaziaException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao alterar fazenda: {str(e)}")

    def listar_fazendas(self):
        try:
            fazendas = list(self.__fazendas_DAO.get_all())
            if not fazendas:
                raise ListaVaziaException("Lista de fazendas vazia")
            
            dados = self._dados_saida_fazenda()
            self.__tela_fazenda.mostra_fazenda_gui(dados)
            
        except ListaVaziaException as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao listar fazendas: {str(e)}")

    def alterar_fazenda_gui(self):
        try:
            fazendas = list(self.__fazendas_DAO.get_all())
            if not fazendas:
                raise ListaVaziaException("Lista de fazendas vazia")

            dados = self._dados_saida_fazenda()

            id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
            if id_fazenda is None:
                raise OperacaoCanceladaException("Nenhuma fazenda selecionada.")
                
            fazenda = self.pega_fazenda_por_id(id_fazenda)
            if fazenda is not None:
                novos_dados_fazenda = self.__tela_fazenda.pega_dados_fazenda()
                if not novos_dados_fazenda:
                    raise OperacaoCanceladaException("Alteração cancelada pelo usuário.")
                    
                fazenda.nome = novos_dados_fazenda["nome"]
                fazenda.id = novos_dados_fazenda["id"]
                fazenda.pais = novos_dados_fazenda["pais"]
                fazenda.estado = novos_dados_fazenda["estado"]
                fazenda.cidade = novos_dados_fazenda["cidade"]
                fazenda.area_plantada = novos_dados_fazenda["area_plantada"]
                
                # Alterar cultura
                self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA NA LISTA:")
                culturas_obj = list(self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all())
                if not culturas_obj:
                    raise ListaVaziaException("Não há culturas cadastradas!")
                    
                culturas = [
                    {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                     "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                     "num_aplicacao": c.num_aplicacao}
                    for c in culturas_obj
                ]
                id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
                nova_cultura = next(
                    (c for c in culturas_obj
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
                raise ItemNaoEncontradoException("Fazenda não encontrada")
                
        except (ListaVaziaException, OperacaoCanceladaException, ItemNaoEncontradoException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao alterar fazenda: {str(e)}")

    def excluir_fazenda_gui(self):
        try:
            fazendas = list(self.__fazendas_DAO.get_all())
            if not fazendas:
                raise ListaVaziaException("Lista de fazendas vazia")

            dados = self._dados_saida_fazenda()

            id_fazenda = self.__tela_fazenda.seleciona_fazenda_gui(dados)
            if id_fazenda is None:
                raise OperacaoCanceladaException("Nenhuma fazenda selecionada.")
                
            fazenda = self.pega_fazenda_por_id(id_fazenda)
            if fazenda is not None:
                self.__fazendas_DAO.remove(id_fazenda)
                self.__tela_fazenda.mostra_mensagem_gui("Fazenda excluída com sucesso!")
                self.listar_fazendas()
            else:
                raise ItemNaoEncontradoException("Fazenda não encontrada")
                
        except (ListaVaziaException, OperacaoCanceladaException, ItemNaoEncontradoException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao excluir fazenda: {str(e)}")

    def gerenciar_fazenda(self):
        try:
            dados = self._dados_saida_fazenda()
            fazenda_id = self.__tela_fazenda.seleciona_fazenda_gui(dados)
            
            if fazenda_id is None:
                raise OperacaoCanceladaException("Nenhuma fazenda selecionada.")

            fazenda = self.pega_fazenda_por_id(fazenda_id)

            if fazenda is not None:
                continua = True
                while continua:
                    try:
                        opcao = self.__tela_fazenda.tela_gerenciador_fazenda()
                        # Gerenciar estoque
                        if opcao == 1:
                            self.__controlador_sistema.controlador_estoque.abre_tela(fazenda.estoque)
                        # Alterar cultura
                        elif opcao == 2:
                            self.__tela_fazenda.mostra_mensagem_gui("SELECIONE UMA NOVA CULTURA NA LISTA:")
                            culturas_obj = list(self.__controlador_sistema.controlador_cultura.culturas_DAO.get_all())
                            if not culturas_obj:
                                raise ListaVaziaException("Não há culturas cadastradas!")
                                
                            culturas = [
                                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento,
                                 "num_aplicacao": c.num_aplicacao}
                                for c in culturas_obj
                            ]
                            id_cultura = self.__controlador_sistema.controlador_cultura.tela_cultura.seleciona_cultura_gui(culturas)
                            nova_cultura = next(
                                (c for c in culturas_obj if
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
                            raise OpcaoNaoExistenteException("Opção inválida.")
                            
                    except (OpcaoNaoExistenteException, ListaVaziaException) as e:
                        self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
                    except Exception as e:
                        self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado no gerenciamento: {str(e)}")
            else:
                raise ItemNaoEncontradoException("Fazenda não encontrada")
                
        except (OperacaoCanceladaException, ItemNaoEncontradoException) as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado ao gerenciar fazenda: {str(e)}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fazenda, 2: self.gerenciar_fazenda,
                        3: self.alterar_fazenda_gui, 4: self.listar_fazendas,
                        5: self.excluir_fazenda_gui, 0: self.retornar}

        continua = True
        while continua:
            try:
                opcao = self.__tela_fazenda.tela_opcoes_gui()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                else:
                    raise OpcaoNaoExistenteException(f"Opção {opcao} não existe.")
                    
            except OpcaoNaoExistenteException as e:
                self.__tela_fazenda.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
            except Exception as e:
                self.__tela_fazenda.mostra_mensagem_gui(f"ERRO inesperado no menu: {str(e)}")
                continua = False  # Sair do loop em caso de erro grave

    def _dados_saida_fazenda(self):
        try:
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
        except Exception as e:
            self.__tela_fazenda.mostra_mensagem_gui(f"ERRO ao preparar dados das fazendas: {str(e)}")
            return []
