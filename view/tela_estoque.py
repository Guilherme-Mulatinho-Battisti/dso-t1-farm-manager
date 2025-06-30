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
            titulo="Produtos no Estoque - ID: " + str(estoque["id"]),  # Convert "id" to string
            lista_itens=
            [f"Produto: {produto} | Quantidade: {quantidade}" for produto, quantidade in estoque["estoque"].items()],
            opcao_retorno="Retornar"
        )

        window = get_janela("Estoque", layout)
        window.read()
        window.close()

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

    def pega_novo_nome_gui(self) -> str:
        layout = [
            [sg.Text("Digite o novo nome do produto:")],
            [sg.Input(key="-NOVO_NOME-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Novo Nome do Produto", layout)
        novo_nome = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                nome = values["-NOVO_NOME-"].strip()
                if not nome:
                    sg.popup_error("O nome não pode ser vazio!")
                    continue
                novo_nome = nome
                break
        window.close()
        return novo_nome

    def pega_nova_quantidade_gui(self) -> int:
        layout = [
            [sg.Text("Digite a nova quantidade:")],
            [sg.Input(key="-NOVA_QTD-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Nova Quantidade", layout)
        quantidade = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                qtd = values["-NOVA_QTD-"].strip()
                if not qtd:
                    sg.popup_error("A quantidade não pode ser vazia!")
                    continue
                try:
                    quantidade = int(qtd)
                except ValueError:
                    sg.popup_error("Digite um número inteiro válido!")
                    continue
                break
        window.close()
        return quantidade

    def mostra_mensagem_gui(self, msg: str):
        sg.popup(msg, title="Mensagem", keep_on_top=True)

    def opcao_alteracao_gui(self) -> int:
        layout = [
            [sg.Text("O que deseja alterar?")],
            [sg.Button("Nome do produto", key="-NOME-"), sg.Button("Quantidade", key="-QTD-")],
            [sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Alterar Estoque", layout)
        opcao = 0
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-NOME-":
                opcao = 1
                break
            if event == "-QTD-":
                opcao = 2
                break
        window.close()
        return opcao

    def seleciona_item_lista_gui(self, lista, titulo="Selecione um item", texto_btn="Selecionar"):
        import FreeSimpleGUI as sg
        if not lista:
            sg.popup("Lista vazia.", title="Aviso", keep_on_top=True)
            return None
        layout = [
            [sg.Listbox(values=lista, size=(40, min(10, len(lista))), key="-ITEM-", select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
            [sg.Button(texto_btn, key="-SELECIONAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela(titulo, layout)
        item_selecionado = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-SELECIONAR-":
                selecionados = values["-ITEM-"]
                if selecionados:
                    item_selecionado = selecionados[0]
                    break
                else:
                    sg.popup_error("Selecione um item da lista!")
        window.close()
        return item_selecionado

    def pega_dados_produto_gui(self, nomes_insumos):
        """Coleta dados de produto e quantidade via GUI"""
        layout = [
            [sg.Text("Selecione um produto:")],
            [sg.Combo(nomes_insumos, key="-PRODUTO-", size=(30, 1), readonly=True)],
            [sg.Text("Digite a quantidade:")],
            [sg.InputText(key="-QUANTIDADE-", size=(20, 1))],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        
        window = get_janela("Adicionar Produto ao Estoque", layout)
        dados = None
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                produto = values["-PRODUTO-"]
                quantidade = values["-QUANTIDADE-"].strip()
                
                if not produto:
                    sg.popup_error("Selecione um produto!")
                    continue
                if not quantidade:
                    sg.popup_error("Digite uma quantidade!")
                    continue
                    
                dados = {"produto": produto, "quantidade": quantidade}
                break
                
        window.close()
        return dados
