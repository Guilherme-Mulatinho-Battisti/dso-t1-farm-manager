from view.tela_operador import TelaOperador
from model.operador import Operador
from model.estoque import Estoque
from model.porto import Porto
from datetime import datetime
from exceptions.custom_exception import (
    OpcaoNaoExistenteException,
    ListaVaziaException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)

class ControladorOperador():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_operador = TelaOperador()
        self.__log = []

    def registrar_log(self, fazenda_estoque, fazenda_id, acao, cultura_nome, area, semente_nome='', implemento_nome='', insumo_nome=''):
        log_entry = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome_fazenda": fazenda_estoque,
            "id_fazenda": fazenda_id,
            "acao": acao,
            "cultura": cultura_nome,
            "area": area,
            "semente": semente_nome,
            "implemento": implemento_nome,
            "insumo": insumo_nome
        }
        self.__log.append(log_entry)

    def comprar_insumo(self, fazenda_estoque: Estoque, porto_estoque: Estoque) -> None:
        try:
            controlador_estoque = self.__controlador_sistema.controlador_estoque

            self.__tela_operador.mostra_mensagem("\n--- Remover insumo do porto ---")
            controlador_estoque.remover_produto_do_estoque(porto_estoque)

            self.__tela_operador.mostra_mensagem("\n--- Adicionar insumo à fazenda ---")
            controlador_estoque.adicionar_produto_ao_estoque(fazenda_estoque)
            
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            self.__tela_operador.mostra_mensagem(f"ERRO na compra de insumo: {str(e)}")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO na compra de insumo: {str(e)}")

    def plantar(self):
        try:
            porto = self.__controlador_sistema.controlador_porto.retornar_porto()
            self.__controlador_sistema.controlador_fazenda.lista_fazendas()
            fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
            if not fazenda:
                raise ItemNaoEncontradoException("Fazenda não encontrada.")

            cultura = fazenda.cultura
            area = fazenda.area_plantada
            fazenda_estoque = fazenda.estoque.estoque

            dose_semente = cultura.dose_semente  # kg/ha
            total_semente_necessaria = dose_semente * area

            # Seleciona semente
            self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
            semente_selecionada = self.__tela_operador.seleciona_insumo()
            if not semente_selecionada:
                self.__tela_operador.mostra_mensagem("Semente indisponivel, por favor compre mais.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            if fazenda_estoque[semente_selecionada] < total_semente_necessaria:
                semente_faltante = total_semente_necessaria - fazenda_estoque[semente_selecionada]
                self.__tela_operador.mostra_mensagem(f"Quantidade de semente insuficiente compre mais {semente_faltante}.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            # Seleciona implemento
            self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
            implemento_selecionado = self.__tela_operador.seleciona_insumo()

            if not implemento_selecionado:
                self.__tela_operador.mostra_mensagem("Nenhum implemento disponível, por favor compre mais.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            # Consome insumos
            fazenda_estoque[semente_selecionada] -= total_semente_necessaria
            fazenda_estoque[implemento_selecionado] -= 1

            self.__tela_operador.mostra_mensagem(f"Plantio da cultura '{cultura.nome}' realizado com sucesso em {area} ha.")
            self.registrar_log(fazenda.nome, fazenda.id, "plantio", cultura.nome, area, semente_selecionada, implemento_selecionado)

        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            self.__tela_operador.mostra_mensagem(f"ERRO no plantio: {str(e)}")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO no plantio: {str(e)}")

    def colher(self):
        try:
            # Implementação da colheita pode ser adicionada aqui
            self.__tela_operador.mostra_mensagem("Funcionalidade de colheita em desenvolvimento.")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO na colheita: {str(e)}")

    def aplicar_insumo(self):
        try:
            self.__tela_operador.mostra_mensagem("\n--- Aplicação de Insumo ---")
            self.__tela_operador.mostra_mensagem("1 - Aplicar Fertilizante")
            self.__tela_operador.mostra_mensagem("2 - Aplicar Defensivo")
            self.__tela_operador.mostra_mensagem("0 - Retornar")
            
            entrada = input("Escolha a opcao: ").strip()
            
            try:
                opcao = int(entrada)
                if opcao == 1:
                    self.aplicar_fertilizante()
                elif opcao == 2:
                    self.aplicar_defensivo()
                elif opcao == 0:
                    return
                else:
                    raise OpcaoNaoExistenteException("Opção inválida para aplicação de insumo.")
            except ValueError:
                raise DadosInvalidosException("Entrada inválida. Digite apenas números.")
                
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            self.__tela_operador.mostra_mensagem(f"ERRO na aplicação de insumo: {str(e)}")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO na aplicação de insumo: {str(e)}")

    def aplicar_fertilizante(self):
        try:
            porto = self.__controlador_sistema.controlador_porto.retornar_porto()
            self.__controlador_sistema.controlador_fazenda.lista_fazendas()
            fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
            if not fazenda:
                raise ItemNaoEncontradoException("Fazenda não encontrada.")

            cultura = fazenda.cultura
            area = fazenda.area_plantada
            fazenda_estoque = fazenda.estoque.estoque

            dose_fertilizante = cultura.dose_fertilizante
            total_fertilizante_necessario = dose_fertilizante * area

            # Seleciona fertilizante
            self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
            fertilizante_id = self.__tela_operador.seleciona_insumo()
            fertilizante_selecionado = fazenda_estoque.get(fertilizante_id)

            if not fertilizante_selecionado:
                self.__tela_operador.mostra_mensagem("Fertilizante indisponível, por favor compre mais.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            if fazenda_estoque[fertilizante_id] < total_fertilizante_necessario:
                falta = total_fertilizante_necessario - fazenda_estoque[fertilizante_id]
                self.__tela_operador.mostra_mensagem(f"Fertilizante insuficiente, compre mais {falta}.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            # Consome insumos
            fazenda_estoque[fertilizante_id] -= total_fertilizante_necessario

            self.__tela_operador.mostra_mensagem(f"Fertilizante aplicado com sucesso na cultura '{cultura.nome}' em {area} ha.")
            self.registrar_log(fazenda.nome, fazenda.id, "aplicação", cultura.nome, area, "", "", fertilizante_selecionado)

        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            self.__tela_operador.mostra_mensagem(f"ERRO na aplicação de fertilizante: {str(e)}")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO na aplicação de fertilizante: {str(e)}")

    def aplicar_defensivo(self):
        try:
            porto = self.__controlador_sistema.controlador_porto.retornar_porto()
            self.__controlador_sistema.controlador_fazenda.lista_fazendas()
            fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
            if not fazenda:
                raise ItemNaoEncontradoException("Fazenda não encontrada.")

            cultura = fazenda.cultura
            area = fazenda.area_plantada
            fazenda_estoque = fazenda.estoque.estoque

            dose_defensivo = cultura.dose_defensivo
            total_defensivo_necessario = dose_defensivo * area

            # Seleciona defensivo
            self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
            defensivo_id = self.__tela_operador.seleciona_insumo()
            defensivo_selecionado = fazenda_estoque.get(defensivo_id)

            if not defensivo_selecionado:
                self.__tela_operador.mostra_mensagem("Defensivo indisponível, por favor compre mais.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            if fazenda_estoque[defensivo_id] < total_defensivo_necessario:
                falta = total_defensivo_necessario - fazenda_estoque[defensivo_id]
                self.__tela_operador.mostra_mensagem(f"Defensivo insuficiente, compre mais {falta}.")
                self.comprar_insumo(fazenda.estoque, porto.estoque)
                return

            # Consome insumos
            fazenda_estoque[defensivo_id] -= total_defensivo_necessario

            self.__tela_operador.mostra_mensagem(f"Defensivo aplicado com sucesso na cultura '{cultura.nome}' em {area} ha.")
            self.registrar_log(fazenda.nome, fazenda.id, "aplicação", cultura.nome, area, "", "", defensivo_selecionado)

        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            self.__tela_operador.mostra_mensagem(f"ERRO na aplicação de defensivo: {str(e)}")
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO na aplicação de defensivo: {str(e)}")

    def retornar(self):
        try:
            self.__controlador_sistema.abre_tela()
        except Exception as e:
            self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO ao retornar: {str(e)}")
            # Em caso de erro crítico, forçar retorno
            self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.plantar, 2: self.colher,
                        3: self.aplicar_insumo, 0: self.retornar}

        continua = True
        while continua:
            try:
                opcao_escolhida = self.__tela_operador.tela_opcoes()
                
                # Verificar se a opção existe
                if opcao_escolhida not in lista_opcoes:
                    raise OpcaoNaoExistenteException(f"Opção {opcao_escolhida} não é válida.")
                
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                
                # Se chegou até aqui e a opção foi 0 (retornar), sair do loop
                if opcao_escolhida == 0:
                    continua = False
                    
            except OpcaoNaoExistenteException as e:
                self.__tela_operador.mostra_mensagem(f"ERRO: {str(e)}")
                continue
            except OperacaoCanceladaException as e:
                self.__tela_operador.mostra_mensagem(f"INFO: {str(e)}")
                continue
            except DadosInvalidosException as e:
                self.__tela_operador.mostra_mensagem(f"ERRO: {str(e)}")
                continue
            except Exception as e:
                self.__tela_operador.mostra_mensagem(f"ERRO INESPERADO: {str(e)}")
                self.__tela_operador.mostra_mensagem("Retornando ao menu do operador...")
                continue
