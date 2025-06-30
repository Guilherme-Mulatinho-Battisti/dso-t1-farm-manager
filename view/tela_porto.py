import FreeSimpleGUI as sg
from .tela_base import TelaBase, get_layout_opcoes, get_janela, get_layout_listagem


class TelaPorto(TelaBase):
    def tela_opcoes(self) -> int:
        while True:
            print("-------- PORTOS ----------")
            print("1 - Gerenciar Estoque Porto")
            print("2 - Alterar Porto")
            print("3 - Mostrar Portos")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None
        try:

            layout = get_layout_opcoes(
                titulo="Portos",
                opcoes=["Gerenciar Estoque", "Alterar Porto", "Mostrar Portos"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Portos", layout)

            event, values = window.read()

            if event == "Gerenciar Estoque":
                opcao = 1
            elif event == "Alterar Porto":
                opcao = 2
            elif event == "Mostrar Portos":
                opcao = 3
            else:
                print("Retornado!")
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e

        finally:
            if window is not None:
                window.close()
            if opcao is None:
                print("Nenhuma opção selecionada. Retornando...")
                opcao = 0

        return opcao

    def tela_gerenciador_estoque_porto(self) -> int:
        while True:
            print("-------- GERENCIADOR ESTOQUE PORTO ----------")
            print("1 - Gerenciar Estoque")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def tela_gerenciador_estoque_porto_gui(self) -> int:
        window, opcao = None, None
        try:
            layout = get_layout_opcoes(
                titulo="Gerenciador Estoque Porto",
                opcoes=["Gerenciar Estoque"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Gerenciador Estoque Porto", layout)

            event, values = window.read()

            if event == "Gerenciar Estoque":
                opcao = 1
            else:
                print("Retornado!")
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e

        finally:
            if window is not None:
                window.close()
            if opcao is None:
                print("Nenhuma opção selecionada. Retornando...")
                opcao = 0

        return opcao

    def pega_dados_porto(self) -> dict:
        print("-------- DADOS PORTO ----------")

        nome = input("Nome: ")
        while not isinstance(nome, str) or nome.strip() == "":
            nome = input("Nome inválido. Digite novamente: ")

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
        }

    def pega_dados_porto_gui(self) -> dict:
        layout = [
            [sg.Text("DADOS DO PORTO", font=("Arial", 14, "bold"))],
            [sg.Text("Nome:"), sg.Input(key="-NOME-")],
            [sg.Text("ID:"), sg.Input(key="-ID-")],
            [sg.Text("País:"), sg.Input(key="-PAIS-")],
            [sg.Text("Estado:"), sg.Input(key="-ESTADO-")],
            [sg.Text("Cidade:"), sg.Input(key="-CIDADE-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Dados do Porto", layout)
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

    def mostra_porto(self, dados_porto: dict) -> None:
        print("Nome da Porto: ", dados_porto["nome"])
        print("Endereço: ", dados_porto["endereco"])
        print("Estoque: ", dados_porto["estoque"])
        print("\n")

    def mostra_portos_gui(self, portos: list) -> None:
        if not portos:
            sg.popup("Nenhum porto cadastrado.")
            return
        layout = get_layout_listagem(
            "Portos",
            [f"Nome: {porto['nome']}\nID: {porto.get('id', '')}\nEndereço: {porto['endereco']}\nEstoque: {porto['estoque']}" for porto in portos],
            "Retornar"
        )
        window = get_janela("Portos", layout)
        window.read()
        window.close()

    def seleciona_porto_gui(self, portos: list) -> int:
        if not portos:
            sg.popup("Nenhum porto cadastrado. Retornando...")
            return None
        layout = [[sg.Text("Selecione o porto desejado:", font=("Arial", 14, "bold"))]]
        for porto in portos:
            texto = f"ID: {porto['id']} | Nome: {porto['nome']}"
            layout.append([
                sg.Text(texto, size=(40, 1)),
                sg.Button("Selecionar", key=f"-SEL-{porto['id']}-")
            ])
        layout.append([sg.Button("Cancelar", key="-CANCELAR-")])
        window = get_janela("Selecionar Porto", layout)
        id_porto = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            for porto in portos:
                if event == f"-SEL-{porto['id']}-":
                    id_porto = porto['id']
                    break
            if id_porto is not None:
                break
        window.close()
        return id_porto

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    def mostra_mensagem_gui(self, msg):
        sg.popup(msg, title="Mensagem", keep_on_top=True)
