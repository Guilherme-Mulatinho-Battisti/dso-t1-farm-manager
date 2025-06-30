from view.tela_porto import TelaPorto
from model.porto import Porto
from model.estoque import Estoque
from model.endereco import Endereco
from exceptions.custom_exception import (
    OpcaoNaoExistenteException,
    ListaVaziaException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)


class ControladorPorto():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__porto = Porto("Brasil", "SP", "Sao Paulo", "Porto Central", Estoque(0, {}))
        self.__tela_porto = TelaPorto()
        self.carrega_dados()

    def retornar_porto(self):
        try:
            if self.__porto is None:
                raise DadosInvalidosException("Porto não está inicializado.")
            return self.__porto
        except DadosInvalidosException as e:
            self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
            return None
        except Exception as e:
            self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado ao retornar porto: {str(e)}")
            return None

    def carrega_dados(self, quantidade_padrao=100):
        try:
            if quantidade_padrao < 0:
                raise DadosInvalidosException("Quantidade padrão não pode ser negativa.")
                
            insumos = self.__controlador_sistema.controlador_insumo.retorna_insumos()
            if not insumos:
                raise ListaVaziaException("Não há insumos cadastrados para carregar no porto.")
                
            for insumo in insumos:
                self.__porto.estoque.estoque[insumo.nome] = quantidade_padrao
                self.__controlador_sistema.controlador_estoque.registrar_log(
                    self.__porto.estoque, "ADICIONADO", insumo.nome, quantidade_padrao
                )
                
        except (DadosInvalidosException, ListaVaziaException) as e:
            self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado ao carregar dados: {str(e)}")

    def alterar_porto(self):
        try:
            porto = self.__porto
            if porto is None:
                raise DadosInvalidosException("Porto não pode ser nulo.")

            novos_dados_porto = self.__tela_porto.pega_dados_porto_gui()
            if not novos_dados_porto:
                raise OperacaoCanceladaException("Alteração cancelada pelo usuário.")

            # Validar dados obrigatórios
            if not novos_dados_porto.get("nome", "").strip():
                raise DadosInvalidosException("Nome do porto é obrigatório.")
            if not novos_dados_porto.get("pais", "").strip():
                raise DadosInvalidosException("País é obrigatório.")
            if not novos_dados_porto.get("estado", "").strip():
                raise DadosInvalidosException("Estado é obrigatório.")
            if not novos_dados_porto.get("cidade", "").strip():
                raise DadosInvalidosException("Cidade é obrigatória.")

            porto.nome = novos_dados_porto["nome"]
            # Alterar endereço usando o método específico
            porto.alterar_endereco(
                novos_dados_porto["pais"], 
                novos_dados_porto["estado"], 
                novos_dados_porto["cidade"]
            )

            self.__tela_porto.mostra_mensagem_gui("Porto alterado com sucesso!")
            self.mostrar_porto()
            
        except (DadosInvalidosException, OperacaoCanceladaException) as e:
            self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado ao alterar porto: {str(e)}")

    def mostrar_porto(self):
        try:
            porto = self.__porto
            if porto is None:
                raise DadosInvalidosException("Porto não pode ser nulo.")
                
            # Criar cópia dos dados do endereço sem passar o objeto original
            endereco_dados = {
                "pais": porto.get_pais(),
                "estado": porto.get_estado(),
                "cidade": porto.get_cidade()
            }
            
            # Criar cópia dos dados do estoque sem passar o objeto original
            estoque_dados = dict(porto.estoque.estoque) if porto.estoque and porto.estoque.estoque else {}
            
            dados = [{
                "nome": str(porto.nome),
                "id": getattr(porto, "id", 0),
                "endereco": endereco_dados,
                "estoque": estoque_dados
            }]
            self.__tela_porto.mostra_portos_gui(dados)
            return True
            
        except DadosInvalidosException as e:
            self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
            return False
        except Exception as e:
            self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado ao mostrar porto: {str(e)}")
            return False

    def gerenciar_estoque_porto(self):
        try:
            porto = self.__porto
            if porto is None:
                raise DadosInvalidosException("Porto não pode ser nulo.")
                
            if porto.estoque is None:
                raise DadosInvalidosException("Estoque do porto não pode ser nulo.")

            self.__controlador_sistema.controlador_estoque.abre_tela(porto.estoque)
            
        except DadosInvalidosException as e:
            self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
        except Exception as e:
            self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado ao gerenciar estoque: {str(e)}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_estoque_porto, 2: self.alterar_porto,
                        3: self.mostrar_porto, 0: self.retornar}

        continua = True
        while continua:
            try:
                opcao = self.__tela_porto.tela_opcoes_gui()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                else:
                    raise OpcaoNaoExistenteException(f"Opção {opcao} não existe.")
                    
            except OpcaoNaoExistenteException as e:
                self.__tela_porto.mostra_mensagem_gui(f"ATENÇÃO: {str(e)}")
            except Exception as e:
                self.__tela_porto.mostra_mensagem_gui(f"ERRO inesperado no menu: {str(e)}")
                continua = False  # Sair do loop em caso de erro grave
