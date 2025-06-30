from view.tela_estoque import TelaEstoque
from model.estoque import Estoque
from datetime import datetime
from functools import partial


class ControladorEstoque:

    def __init__(self, controlador_sistema):
        self.__estoques = []
        self.__tela_estoque = TelaEstoque()
        self.__controlador_sistema = controlador_sistema

    def registrar_log(self, estoque, acao, produto, quantidade=None):
        log_entry = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "acao": acao,
            "produto": produto,
            "quantidade": quantidade
        }
        estoque.log.append(log_entry)

    def adicionar_produto_ao_estoque(self, estoque):
        insumos = self.__controlador_sistema.controlador_insumo.retorna_insumos()
        if not insumos:
            self.__tela_estoque.mostra_mensagem("Não há insumos cadastrados.")
            return
        nomes_insumos = [insumo.nome for insumo in insumos]

        self.__controlador_sistema.controlador_insumo.lista_insumo()

        dados = self.__tela_estoque.pega_dados_produto_gui(nomes_insumos)
        if not dados or not dados.get("produto"):
            return
        produto = dados["produto"]
        quantidade = dados.get("quantidade")
        if produto not in nomes_insumos:
            self.__tela_estoque.mostra_mensagem("Produto inválido. Escolha um dos insumos cadastrados.")
            return
        
        try:
            quantidade = int(quantidade)
            estoque.estoque[produto] = quantidade
            self.registrar_log(estoque, "ADICIONADO", produto, quantidade)
            self.__tela_estoque.mostra_mensagem(f"Produto '{produto}' adicionado/atualizado com sucesso.")
        except (ValueError, TypeError):
            self.__tela_estoque.mostra_mensagem("Quantidade inválida.")

    def remover_produto_do_estoque(self, estoque):
        if not estoque.estoque:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return

        self.__tela_estoque.mostra_estoque_gui(estoque.estoque)
        produto = self.__tela_estoque.seleciona_item_lista_gui(estoque.estoque)

        if produto in estoque.estoque:
            del estoque.estoque[produto]
            self.registrar_log(estoque, "REMOVIDO", produto)
            self.__tela_estoque.mostra_mensagem(f"Produto '{produto}' removido com sucesso.")
        else:
            self.__tela_estoque.mostra_mensagem("Produto não encontrado.")

    def alterar_estoque(self, estoque):
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("ATENÇÃO: estoque não existente")
            return

        if not estoque.estoque:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return

        produto_selecionado = self.__tela_estoque.seleciona_item_lista_gui(estoque.estoque)
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

    def mostra_estoque(self, estoque):
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("ATENÇÃO: estoque não existente")
            return

        self.__tela_estoque.mostra_estoque_gui({"id": estoque.id, "estoque": estoque.estoque})

    def limpar_estoque(self, estoque):

        if estoque is not None:
            estoque.estoque.clear()  # esvazia o dicionário de produtos
            self.__tela_estoque.mostra_mensagem("Estoque limpo com sucesso.")
            self.mostra_estoque(estoque)
        else:
            self.__tela_estoque.mostra_mensagem("ATENÇÃO: estoque não existente.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self, estoque):
        lista_opcoes = {
            1: partial(self.adicionar_produto_ao_estoque, estoque),
            2: partial(self.remover_produto_do_estoque, estoque),
            3: partial(self.mostra_estoque, estoque),
            4: partial(self.alterar_estoque, estoque),
            5: partial(self.limpar_estoque, estoque),
            0: self.retornar
        }

        while True:
            opcao = self.__tela_estoque.tela_opcoes_gui()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_estoque.mostra_mensagem("Opção inválida.")
