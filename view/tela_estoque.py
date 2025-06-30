class TelaEstoque:
    def tela_gerenciador_estoque(self) -> int:
        print("-------- GERENCIADOR DE ESTOQUE ----------")
        print("Escolha a opcao")
        print("1 - Adicionar Produto ao Estoque")
        print("2 - Remover Produto do Estoque")
        print("3 - Mostrar Produtos no Estoque")
        print("4 - Alterar Estoque")
        print("5 - Limpar Estoque")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_estoque(self, estoque: dict):
        print("\nProdutos no estoque:")
        print(f"ID do Estoque: {estoque['id']}")
        if not estoque["estoque"]:
            print("Estoque vazio.")
            return
        for produto, quantidade in estoque["estoque"].items():
            print(f"- Produto: {produto} | Quantidade: {quantidade}")
        print("\n")

    def seleciona_produto(self) -> str:
        produto = input("Digite o nome do produto que deseja alterar: ").strip()
        return produto

    def opcao_alteracao(self) -> int:
        print("\nO que deseja alterar?")
        print("1 - Nome do produto")
        print("2 - Quantidade")
        print("0 - Cancelar")

        while True:
            try:
                opcao = int(input("Escolha a opção: ").strip())
                if opcao in [1, 2]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 2.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

    def pega_novo_nome(self) -> str:
        novo_nome = input("Digite o novo nome do produto: ").strip()
        return novo_nome

    def pega_nova_quantidade(self) -> int:
        while True:
            try:
                quantidade = int(input("Digite a nova quantidade: ").strip())
                return quantidade
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    def mostra_mensagem(self, msg: str):
        print(f"\n{msg}\n")
