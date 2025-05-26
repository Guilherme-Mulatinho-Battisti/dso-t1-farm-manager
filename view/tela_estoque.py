class TelaEstoque():
    def tela_opcoes(self) -> int:
        print("-------- ESTOQUES ----------")
        print("Escolha a opcao")
        print("1 - Adicionar Existente")
        print("2 - Adicionar Produto Novo")
        print("3 - Remover Produtos")
        print("4 - Listar Estoques")
        print("5 - Excluir Estoque")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_gerenciador_estoque(self) -> int:
        print("-------- GERENCIADOR DE ESTOQUE ----------")
        print("Escolha a opcao")
        print("1 - Adicionar Produto ao Estoque")
        print("2 - Remover Produto do Estoque")
        print("3 - Listar Produtos no Estoque")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_estoque(self, estoque: dict) -> None:
        for produto, quantidade in estoque.items():
            print(f"Produto: {produto}, Quantidade: {quantidade}")
        print("\n")

    def mostra_mensagem(self, msg) -> None:
        print(msg)
