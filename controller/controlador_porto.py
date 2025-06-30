from view.tela_porto import TelaPorto
from model.porto import Porto
from model.estoque import Estoque
from model.endereco import Endereco


class ControladorPorto():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__porto = Porto("Brasil", "SP", "Sao Paulo", "Porto Central", Estoque(0, {}))
        self.__tela_porto = TelaPorto()
        self.carrega_dados()

    def retornar_porto(self):
        return self.__porto

    def carrega_dados(self, quantidade_padrao=100):
        insumos = self.__controlador_sistema.controlador_insumo.retorna_insumos()
        for insumo in insumos:
            self.__porto.estoque.estoque[insumo.nome] = quantidade_padrao
            self.__controlador_sistema.controlador_estoque.registrar_log(
                self.__porto.estoque, "ADICIONADO", insumo.nome, quantidade_padrao
            )

    def alterar_porto(self):
        porto = self.__porto
        if porto is None:
            return

        novos_dados_porto = self.__tela_porto.pega_dados_porto_gui()
        if not novos_dados_porto:
            self.__tela_porto.mostra_mensagem_gui("Alteração cancelada.")
            return

        porto.nome = novos_dados_porto["nome"]
        porto.endereco = (novos_dados_porto["pais"], novos_dados_porto["estado"], novos_dados_porto["cidade"])

        self.__tela_porto.mostra_mensagem_gui("Porto alterado com sucesso!")
        self.mostrar_porto()

    def mostrar_porto(self):
        porto = self.__porto
        dados = [{
            "nome": porto.nome,
            "id": getattr(porto, "id", 0),
            "endereco": f"{porto.endereco[0]}, {porto.endereco[1]}, {porto.endereco[2]}",
            "estoque": porto.estoque.estoque
        }]
        self.__tela_porto.mostra_portos_gui(dados)
        return self.__porto

    def gerenciar_estoque_porto(self):
        porto = self.__porto

        if porto is None:
            return

        self.__controlador_sistema.controlador_estoque.abre_tela(porto.estoque)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_estoque_porto, 2: self.alterar_porto,
                        3: self.mostrar_porto, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_porto.tela_opcoes_gui()]()
