from view.tela_estoque import TelaEstoque
from model.estoque import Estoque

class ControladorEstoque():

    def __init__(self, controlador_sistema):
        self.__estoques = []
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def adicionar_produto_ao_estoque(self, estoque):
        self.__controlador_sistema.controlador_insumo.lista_insumo()
        while True:
            produto = input("Digite o nome do produto (ou ENTER para sair): ").strip()
            if not produto:
                break
            try:
                quantidade = int(input("Digite a quantidade: ").strip())
                estoque.estoque[produto] = quantidade
            except ValueError:
                print("Quantidade inválida.")

    def remover_produto_do_estoque(self, estoque):
        if not estoque.estoque:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return

        self.__tela_estoque.mostra_estoque(estoque.estoque)
        produto = self.__tela_estoque.seleciona_produto(estoque.estoque)

        if produto in estoque.estoque:
            del estoque.estoque[produto]
            self.__tela_estoque.mostra_mensagem(f"Produto '{produto}' removido com sucesso.")
        else:
            self.__tela_estoque.mostra_mensagem("Produto não encontrado.")

    def alterar_estoque(self):
        self.lista_estoques()
        id_estoque = self.__tela_estoque.seleciona_estoque()
        estoque = self.pega_estoque_por_id(id_estoque)

        if estoque is None:
            self.__tela_estoque.mostra_mensagem("ATENÇÃO: estoque não existente")
            return

        if not estoque.estoque:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return

        self.__tela_estoque.mostra_estoque(estoque.estoque)

        produto_selecionado = self.__tela_estoque.seleciona_produto(estoque.estoque)
        if produto_selecionado not in estoque.estoque:
            self.__tela_estoque.mostra_mensagem("Produto não encontrado.")
            return

        opcao = self.__tela_estoque.opcao_alteracao()
        if opcao == 1:
            novo_nome = self.__tela_estoque.pega_novo_nome()
            quantidade = estoque.estoque[produto_selecionado]
            del estoque.estoque[produto_selecionado]
            estoque.estoque[novo_nome] = quantidade
        elif opcao == 2:
            nova_quantidade = self.__tela_estoque.pega_nova_quantidade()
            estoque.estoque[produto_selecionado] = nova_quantidade
        else:
            self.__tela_estoque.mostra_mensagem("Opção inválida.")
            return

        self.__tela_estoque.mostra_mensagem("Produto atualizado com sucesso.")

    def lista_estoques(self):
        if len(self.__estoques) == 0:
            self.__tela_estoque.mostra_mensagem("ATENCAO: lista de estoques vazia")
            return

        for estoque in self.__estoques:
            self.__tela_estoque.mostra_estoque({"id": estoque.id, "estoque": estoque.estoque})

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

    def abre_tela(self, estoque):
        lista_opcoes = {1: self.adicionar_produto_ao_estoque(estoque), 2: self.remover_produto_do_estoque(estoque),
                        3: self.lista_estoques, 4: self.alterar_estoque,
                        5: self.limpar_estoque, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes_gerenciar_estoque()]()
