class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto} adicionado ao estoque.")

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print(f"Produto {produto} removido do estoque.")
        else:
            print(f"Produto {produto} não encontrado no estoque.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto no estoque.")
        else:
            print("Produtos no estoque:")
            for produto in self.produtos:
                print(f"- {produto}")