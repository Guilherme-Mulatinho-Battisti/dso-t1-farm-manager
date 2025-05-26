class Estoque:
    """ - id : Por padrão, o estoque recebe o ID do local.
        - estoque: dict do tipo {produto: quantidade}"""
    def __init__(self, id: int, estoque: dict = {}):
        self.id = id
        self.estoque = estoque  # 

    def adicionar_produto(self, produto, quantidade=1):
        if produto in self.estoque:
            self.estoque[produto] += quantidade
        else:
            self.estoque[produto] = quantidade
        print(f"{quantidade}x {produto} adicionado(s) ao estoque.")

    def remover_produto(self, produto, quantidade=1):
        if produto in self.estoque:
            self.estoque[produto] -= quantidade
            if self.estoque[produto] <= 0:
                del self.estoque[produto]
            print(f"{quantidade}x {produto} removido(s) do estoque.")
        else:
            print(f"Produto {produto} não encontrado no estoque.")

    def listar_produtos(self):
        if not self.estoque:
            print("Nenhum produto no estoque.")
        else:
            print("Produtos no estoque:")
            for produto, qtd in self.estoque.items():
                print(f"- {produto}: {qtd} unidade(s)")
