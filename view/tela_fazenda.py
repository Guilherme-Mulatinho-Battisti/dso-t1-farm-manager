from typing import Any

from view.tela_base import get_layout_opcoes, TelaBase, get_janela, get_layout_listagem
import FreeSimpleGUI as sg


class TelaFazenda(TelaBase):
    def tela_opcoes(self) -> int:
        while True:
            print("-------- FAZENDAS ----------")
            print("1 - Incluir Fazenda")
            print("2 - Gerenciar Fazenda")
            print("3 - Alterar Fazenda")
            print("4 - Listar Fazendas")
            print("5 - Excluir Fazenda")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None

        try:
            layout = get_layout_opcoes(
                titulo="Fazendas",
                opcoes=["Incluir Fazenda", "Gerenciar Fazenda", "Alterar Fazenda", "Listar Fazendas",
                        "Excluir Fazenda"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Fazendas", layout)
            event, values = window.read()

            if event == "Incluir Fazenda":
                opcao = 1
            elif event == "Gerenciar Fazenda":
                opcao = 2
            elif event == "Alterar Fazenda":
                opcao = 3
            elif event == "Listar Fazendas":
                opcao = 4
            elif event == "Excluir Fazenda":
                opcao = 5
            else:
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e

        finally:
            if window is not None:
                window.close()

        return opcao

    def tela_gerenciador_fazenda(self) -> int:
        while True:
            print("-------- GERENCIADOR DE FAZENDA ----------")
            print("1 - Gerenciar Estoque")
            print("2 - Alterar Cultura")
            print("3 - Plantar")
            print("4 - Colher")
            print("5 - Aplicar Defensivo")
            print("6 - Aplicar Fertilizante")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5, 6]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def pega_dados_fazenda(self) -> dict:
        print("-------- DADOS FAZENDA ----------")

        nome = input("Nome: ")
        while not isinstance(nome, str) or nome.strip() == "":
            nome = input("Nome inválido. Digite novamente: ")

        while True:
            try:
                id = int(input("ID (número inteiro): "))
                break
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

        while True:
            try:
                area = int(input("Área Plantada (em ha - número inteiro): "))
                break
            except ValueError:
                print("Área inválida. Digite um número inteiro.")

        print("--- ENDEREÇO ---")

        pais = input("País: ")
        while not isinstance(pais, str) or pais.strip() == "":
            pais = input("País inválido. Digite novamente: ")

        estado = input("Estado: ")
        while not isinstance(estado, str) or estado.strip() == "":
            estado = input("Estado inválido. Digite novamente: ")

        cidade = input("Cidade: ")
        while not isinstance(cidade, str) or cidade.strip() == "":
            cidade = input("Cidade inválida. Digite novamente: ")

        return {
            "nome": nome.strip(),
            "id": id,
            "pais": pais.strip(),
            "estado": estado.strip(),
            "cidade": cidade.strip(),
            "area_plantada": area,
        }

    def mostra_fazenda(self, dados_fazenda: dict) -> None:
        print("Nome da Fazenda: ", dados_fazenda["nome"])
        print("ID da Fazenda: ", dados_fazenda["id"])
        print("Endereço: ", dados_fazenda["endereco"])
        print("Area Plantada: ", dados_fazenda["area_plantada"])
        print("Cultura: ", dados_fazenda["cultura"])
        print("Estoque: ", dados_fazenda["estoque"])
        print("\n")

    def pega_dados_fazenda_gui(self) -> dict:
        layout = [
            [sg.Text("DADOS DA FAZENDA", font=("Arial", 14, "bold"))],
            [sg.Text("Nome:"), sg.Input(key="-NOME-")],
            [sg.Text("ID:"), sg.Input(key="-ID-")],
            [sg.Text("Área Plantada (ha):"), sg.Input(key="-AREA-")],
            [sg.Text("País:"), sg.Input(key="-PAIS-")],
            [sg.Text("Estado:"), sg.Input(key="-ESTADO-")],
            [sg.Text("Cidade:"), sg.Input(key="-CIDADE-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Dados da Fazenda", layout)
        dados = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                if not values["-NOME-"] or not values["-ID-"]:
                    sg.popup_error("Nome e ID são obrigatórios!")
                    continue
                try:
                    dados = {
                        "nome": values["-NOME-"],
                        "id": int(values["-ID-"]),
                        "area_plantada": int(values["-AREA-"]),
                        "pais": values["-PAIS-"],
                        "estado": values["-ESTADO-"],
                        "cidade": values["-CIDADE-"]
                    }
                except Exception:
                    sg.popup_error("Preencha todos os campos corretamente!")
                    continue
                break
        window.close()
        return dados

    def seleciona_fazenda_gui(self, fazendas: list) -> Any | None:
        if not fazendas:
            sg.popup("Nenhuma fazenda cadastrada. Retornando...")
            return None

        layout = [[sg.Text("Selecione a fazenda desejada:", font=("Arial", 14, "bold"))]]
        for fazenda in fazendas:
            texto = f"ID: {fazenda['id']} | Nome: {fazenda['nome']}"
            layout.append([
                sg.Text(texto, size=(40, 1)),
                sg.Button("Selecionar", key=f"-SEL-{fazenda['id']}-")
            ])
        layout.append([sg.Button("Cancelar", key="-CANCELAR-")])
        window = get_janela("Selecionar Fazenda", layout)
        id_fazenda = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            for fazenda in fazendas:
                if event == f"-SEL-{fazenda['id']}-":
                    id_fazenda = fazenda['id']
                    break
            if id_fazenda is not None:
                break
        window.close()
        return id_fazenda

    def mostra_mensagem_gui(self, msg):
        sg.popup(msg, title="Mensagem", keep_on_top=True)

    def mostra_fazenda_gui(self, dados_fazendas: list) -> None:
        if not dados_fazendas:
            sg.popup("Nenhuma fazenda encontrada. Retornando...")
            return
        linhas = []
        for dado in dados_fazendas:
            linhas.append(
                f"Nome: {dado['nome']}\nID: {dado['id']}\nEndereço: {dado['pais']}, {dado['estado']}, {dado['cidade']}\n"
                f"Área Plantada: {dado['area_plantada']} ha\nCultura: {dado.get('cultura', '')}\nEstoque: {dado.get('estoque', '')}"
            )
        layout = get_layout_listagem("Fazendas", linhas, "Retornar")
        window = get_janela("Fazendas", layout)
        window.read()
        window.close()

    def seleciona_fazenda(self) -> int:
        while True:
            try:
                id = int(input("ID do fazenda que deseja selecionar: "))
                return id
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def mostra_mensagem(self, msg) -> None:
        print(msg)
