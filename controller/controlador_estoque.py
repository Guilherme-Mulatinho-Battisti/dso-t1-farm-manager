from view.tela_estoque import TelaEstoque
from model.estoque import Estoque
from datetime import datetime
from functools import partial
from exceptions.custom_exception import (
    OpcaoNaoExistenteException,
    ListaVaziaException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)


class ControladorEstoque:

    def __init__(self, controlador_sistema):
        self.__estoques = []
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def registrar_log(self, estoque, acao, produto, quantidade=None):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")
            if not acao or not produto:
                raise DadosInvalidosException("Ação e produto são obrigatórios.")
                
            log_entry = {
                "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "acao": acao,
                "produto": produto,
                "quantidade": quantidade
            }
            estoque.log.append(log_entry)
            
        except DadosInvalidosException as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO no log: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado no log: {str(e)}")

    def adicionar_produto_ao_estoque(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")
                
            insumos = self.__controlador_sistema.controlador_insumo.retorna_insumos()
            if not insumos:
                raise ListaVaziaException("Não há insumos cadastrados.")
                
            nomes_insumos = [insumo.nome for insumo in insumos]

            self.__controlador_sistema.controlador_insumo.lista_insumo()

            dados = self.__tela_estoque.pega_dados_produto_gui(nomes_insumos)
            if not dados or not dados.get("produto"):
                raise OperacaoCanceladaException("Operação cancelada pelo usuário.")
                
            produto = dados["produto"]
            quantidade = dados.get("quantidade")
            
            if not quantidade:
                raise DadosInvalidosException("Quantidade é obrigatória.")
            
            if produto not in nomes_insumos:
                raise ItemNaoEncontradoException("Produto inválido. Escolha um dos insumos cadastrados.")
            
            try:
                quantidade = int(quantidade)
                if quantidade < 0:
                    raise DadosInvalidosException("Quantidade não pode ser negativa.")
                    
                estoque.estoque[produto] = quantidade
                self.registrar_log(estoque, "ADICIONADO", produto, quantidade)
                self.__tela_estoque.mostra_mensagem(f"Produto '{produto}' adicionado/atualizado com sucesso.")
                
            except (ValueError, TypeError):
                raise DadosInvalidosException("Quantidade deve ser um número válido.")
                
        except (DadosInvalidosException, ListaVaziaException, OperacaoCanceladaException, ItemNaoEncontradoException) as e:
            self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao adicionar produto: {str(e)}")

    def remover_produto_do_estoque(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")
                
            if not estoque.estoque:
                raise ListaVaziaException("Estoque vazio.")

            self.__tela_estoque.mostra_estoque_gui(estoque.estoque)
            produto = self.__tela_estoque.seleciona_item_lista_gui(estoque.estoque)

            if not produto:
                raise OperacaoCanceladaException("Nenhum produto selecionado.")

            if produto in estoque.estoque:
                del estoque.estoque[produto]
                self.registrar_log(estoque, "REMOVIDO", produto)
                self.__tela_estoque.mostra_mensagem(f"Produto '{produto}' removido com sucesso.")
            else:
                raise ItemNaoEncontradoException("Produto não encontrado.")
                
        except (DadosInvalidosException, ListaVaziaException, OperacaoCanceladaException, ItemNaoEncontradoException) as e:
            self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao remover produto: {str(e)}")

    def alterar_estoque(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")

            if not estoque.estoque:
                raise ListaVaziaException("Estoque vazio.")

            produto_selecionado = self.__tela_estoque.seleciona_item_lista_gui(estoque.estoque)
            if not produto_selecionado:
                raise OperacaoCanceladaException("Nenhum produto selecionado.")
                
            if produto_selecionado not in estoque.estoque:
                raise ItemNaoEncontradoException("Produto não encontrado.")

            opcao = self.__tela_estoque.opcao_alteracao()
            if opcao == 1:
                novo_nome = self.__tela_estoque.pega_novo_nome()
                if not novo_nome:
                    raise OperacaoCanceladaException("Nome não informado.")
                quantidade = estoque.estoque[produto_selecionado]
                del estoque.estoque[produto_selecionado]
                estoque.estoque[novo_nome] = quantidade
                self.registrar_log(estoque, "ALTERADO NOME", f"{produto_selecionado} -> {novo_nome}")
            elif opcao == 2:
                nova_quantidade = self.__tela_estoque.pega_nova_quantidade()
                if nova_quantidade is None:
                    raise OperacaoCanceladaException("Quantidade não informada.")
                if nova_quantidade < 0:
                    raise DadosInvalidosException("Quantidade não pode ser negativa.")
                estoque.estoque[produto_selecionado] = nova_quantidade
                self.registrar_log(estoque, "ALTERADO QUANTIDADE", produto_selecionado, nova_quantidade)
            else:
                raise OpcaoNaoExistenteException("Opção inválida.")

            self.__tela_estoque.mostra_mensagem("Produto atualizado com sucesso.")
            
        except (DadosInvalidosException, ListaVaziaException, OperacaoCanceladaException, 
                ItemNaoEncontradoException, OpcaoNaoExistenteException) as e:
            self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao alterar estoque: {str(e)}")

    def mostra_estoque(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")

            self.__tela_estoque.mostra_estoque_gui({"id": estoque.id, "estoque": estoque.estoque})
            
        except DadosInvalidosException as e:
            self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao mostrar estoque: {str(e)}")

    def limpar_estoque(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")
                
            if not estoque.estoque:
                raise ListaVaziaException("Estoque já está vazio.")

            estoque.estoque.clear()  # esvazia o dicionário de produtos
            self.registrar_log(estoque, "LIMPO", "TODOS OS PRODUTOS")
            self.__tela_estoque.mostra_mensagem("Estoque limpo com sucesso.")
            self.mostra_estoque(estoque)
            
        except (DadosInvalidosException, ListaVaziaException) as e:
            self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao limpar estoque: {str(e)}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self, estoque):
        try:
            if estoque is None:
                raise DadosInvalidosException("Estoque não pode ser nulo.")
                
            lista_opcoes = {
                1: partial(self.adicionar_produto_ao_estoque, estoque),
                2: partial(self.remover_produto_do_estoque, estoque),
                3: partial(self.mostra_estoque, estoque),
                4: partial(self.alterar_estoque, estoque),
                5: partial(self.limpar_estoque, estoque),
                0: self.retornar
            }

            while True:
                try:
                    opcao = self.__tela_estoque.tela_opcoes_gui()
                    funcao = lista_opcoes.get(opcao)
                    if funcao:
                        funcao()
                    else:
                        raise OpcaoNaoExistenteException(f"Opção {opcao} não existe.")
                        
                except OpcaoNaoExistenteException as e:
                    self.__tela_estoque.mostra_mensagem(f"ATENÇÃO: {str(e)}")
                except Exception as e:
                    self.__tela_estoque.mostra_mensagem(f"ERRO inesperado no menu: {str(e)}")
                    
        except DadosInvalidosException as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO: {str(e)}")
        except Exception as e:
            self.__tela_estoque.mostra_mensagem(f"ERRO inesperado ao abrir tela: {str(e)}")
