from view.tela_estoque import TelaEstoque
from model.estoque import Estoque

class ControladorEstoque():

    def __init__(self, controlador_sistema):
        self.__estoques = []
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def alterar_estoque(self):
        self.lista_estoques()
        id_estoque = self.__tela_estoque.seleciona_estoque()
        estoque = self.pega_estoque_por_id(id_estoque)

        if (estoque is not None):
            novos_dados_estoque = self.__tela_estoque.pega_dados_estoque()
            estoque.nome = novos_dados_estoque["nome"]
            estoque.telefone = novos_dados_estoque["telefone"]
            estoque.id = novos_dados_estoque["id"]
            self.lista_estoques()
        else:
            self.__tela_estoque.mostra_mensagem("ATENCAO: estoque não existente")

    def lista_estoques(self):
        if len(self.__estoques) == 0:
            self.__tela_estoque.mostra_mensagem("ATENCAO: lista de estoques vazia")
            return

        for estoque in self.__estoques:
            self.__tela_estoque.mostra_estoque({"nome": estoque.nome, "id": estoque.id,
                                                "dose_semente": estoque.dose_semente,
                                                "dose_fertilizante": estoque.dose_fertilizante,
                                                "dose_defensivo": estoque.dose_defensivo,
                                                "temp_crescimento": estoque.temp_crescimento,
                                                "num_aplicacao": estoque.num_aplicacao})

    def limpar_estoque(self):
        self.lista_estoques()
        id_estoque = self.__tela_estoque.seleciona_estoque()
        estoque = self.pega_estoque_por_id(id_estoque)

        if estoque is not None:
            estoque.estoque.clear()  # esvazia o dicionário de produtos
            self.__tela_estoque.mostra_mensagem("Estoque limpo com sucesso.")
            self.lista_estoques()
        else:
            self.__tela_estoque.mostra_mensagem("ATENÇÃO: estoque não existente.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_estoque, 2: self.alterar_estoque,
                        3: self.lista_estoques, 4: self.excluir_estoque,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes()]()
