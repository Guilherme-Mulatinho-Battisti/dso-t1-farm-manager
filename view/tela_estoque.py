from view.tela_base import get_janela, get_layout_opcoes, get_layout_listagem
import FreeSimpleGUI as sg


class TelaEstoque:
    def tela_opcoes(self) -> int:
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

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None

        try:
            layout = get_layout_opcoes(
                titulo="Gerenciador de Estoque",
                opcoes=[
                    "Adicionar Produto ao Estoque",
                    "Remover Produto do Estoque",
                    "Mostrar Produtos no Estoque",
                    "Alterar Estoque",
                    "Limpar Estoque"
                ],
                opcao_retorno="Retornar"
            )

            window = get_janela("Gerenciador de Estoque", layout)
            event, values = window.read()

            if event == "Adicionar Produto ao Estoque":
                opcao = 1
            elif event == "Remover Produto do Estoque":
                opcao = 2
            elif event == "Mostrar Produtos no Estoque":
                opcao = 3
            elif event == "Alterar Estoque":
                opcao = 4
            elif event == "Limpar Estoque":
                opcao = 5
            else:
                print("Retornado!")
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar: {e}") from e
        finally:
            if window is not None:
                window.close()
            if opcao is None:
                print("Nenhuma opção selecionada. Retornando...")
                opcao = 0

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

    def mostra_estoque_gui(self, estoque: dict) -> None:
        if not estoque["estoque"]:
            sg.popup("Estoque vazio.")
            return

        layout = get_layout_listagem(
            titulo="Produtos no Estoque - ID: " + estoque["id"],
            lista_itens=
            [f"Produto: {produto} | Quantidade: {quantidade}" for produto, quantidade in estoque["estoque"].items()],
            opcao_retorno="Retornar"
        )

        window = get_janela("Estoque", layout)
        window.read()
        window.close()

    def seleciona_produto(self, estoque: dict) -> str:
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
