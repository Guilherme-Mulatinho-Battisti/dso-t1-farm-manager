from view.tela_sistema import TelaSistema
from controller.controlador_cultura import ControladorCultura
from controller.controlador_insumo import ControladorInsumo
from controller.controlador_fazenda import ControladorFazenda
from controller.controlador_estoque import ControladorEstoque
from controller.controlador_operador import ControladorOperador
from controller.controlador_porto import ControladorPorto

class ControladorSistema:

    def __init__(self):
        self.__controlador_insumo = ControladorInsumo(self)
        self.__controlador_cultura = ControladorCultura(self)
        self.__controlador_fazenda = ControladorFazenda(self)
        self.__controlador_estoque = ControladorEstoque(self)
        self.__controlador_operador = ControladorOperador(self)
        self.__controlador_porto = ControladorPorto(self)
        self.__tela_sistema = TelaSistema()

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
        self.abre_tela()

    def cadastra_insumo(self):
        # Chama o controlador de insumo
        self.__controlador_insumo.abre_tela()

    def cadastra_cultura(self):
        # Chama o controlador de cultura
        self.__controlador_cultura.abre_tela()

    def cadastra_fazenda(self):
        # Chama o controlador de fazenda
        self.__controlador_fazenda.abre_tela()

    def cadastrar_porto(self):
        # Chama o controlador de fazenda
        self.__controlador_porto.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_insumo, 2: self.cadastra_cultura,
                        3: self.cadastra_fazenda, 4: self.cadastrar_porto,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_gui()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
