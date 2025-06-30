from view.tela_sistema import TelaSistema
from controller.controlador_cultura import ControladorCultura
from controller.controlador_insumo import ControladorInsumo
from controller.controlador_fazenda import ControladorFazenda
from controller.controlador_estoque import ControladorEstoque
from controller.controlador_operador import ControladorOperador
from controller.controlador_porto import ControladorPorto
from exceptions.custom_exception import (
    OpcaoNaoExistenteException,
    ListaVaziaException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)

class ControladorSistema:

    def __init__(self):
        try:
            self.__controlador_insumo = ControladorInsumo(self)
            self.__controlador_cultura = ControladorCultura(self)
            self.__controlador_fazenda = ControladorFazenda(self)
            self.__controlador_estoque = ControladorEstoque(self)
            self.__controlador_operador = ControladorOperador(self)
            self.__controlador_porto = ControladorPorto(self)
            self.__tela_sistema = TelaSistema()
            
        except Exception as e:
            print(f"ERRO CRÍTICO ao inicializar sistema: {str(e)}")
            raise  # Re-propagar a exceção pois é crítica

    @property
    def controlador_insumo(self):
        return self.__controlador_insumo

    @property
    def controlador_cultura(self):
        return self.__controlador_cultura

    @property
    def controlador_fazenda(self):
        return self.__controlador_fazenda

    @property
    def controlador_estoque(self):
        return self.__controlador_estoque

    @property
    def controlador_operador(self):
        return self.__controlador_operador

    @property
    def controlador_porto(self):
        return self.__controlador_porto

    def inicializa_sistema(self):
        try:
            self.abre_tela()
        except Exception as e:
            print(f"ERRO CRÍTICO ao inicializar sistema: {str(e)}")
            self.encerra_sistema()

    def cadastra_insumo(self):
        try:
            # Chama o controlador de insumo
            self.__controlador_insumo.abre_tela()
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            print(f"ERRO no cadastro de insumo: {str(e)}")
        except Exception as e:
            print(f"ERRO INESPERADO no cadastro de insumo: {str(e)}")

    def cadastra_cultura(self):
        try:
            # Chama o controlador de cultura
            self.__controlador_cultura.abre_tela()
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            print(f"ERRO no cadastro de cultura: {str(e)}")
        except Exception as e:
            print(f"ERRO INESPERADO no cadastro de cultura: {str(e)}")

    def cadastra_fazenda(self):
        try:
            # Chama o controlador de fazenda
            self.__controlador_fazenda.abre_tela()
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            print(f"ERRO no cadastro de fazenda: {str(e)}")
        except Exception as e:
            print(f"ERRO INESPERADO no cadastro de fazenda: {str(e)}")

    def cadastrar_porto(self):
        try:
            # Chama o controlador de porto
            self.__controlador_porto.abre_tela()
        except (OpcaoNaoExistenteException, ListaVaziaException, 
                ItemNaoEncontradoException, DadosInvalidosException, 
                OperacaoCanceladaException) as e:
            print(f"ERRO no cadastro de porto: {str(e)}")
        except Exception as e:
            print(f"ERRO INESPERADO no cadastro de porto: {str(e)}")

    def encerra_sistema(self):
        try:
            print("Encerrando sistema...")
            exit(0)
        except Exception as e:
            print(f"ERRO ao encerrar sistema: {str(e)}")
            exit(1)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_insumo, 2: self.cadastra_cultura,
                        3: self.cadastra_fazenda, 4: self.cadastrar_porto,
                        0: self.encerra_sistema}

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_gui()
                
                # Verificar se a opção existe
                if opcao_escolhida not in lista_opcoes:
                    raise OpcaoNaoExistenteException(f"Opção {opcao_escolhida} não é válida.")
                
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                
            except OpcaoNaoExistenteException as e:
                print(f"ERRO: {str(e)}")
                continue
            except OperacaoCanceladaException as e:
                print(f"INFO: {str(e)}")
                continue
            except DadosInvalidosException as e:
                print(f"ERRO: {str(e)}")
                continue
            except Exception as e:
                print(f"ERRO INESPERADO: {str(e)}")
                print("Retornando ao menu principal...")
                continue
