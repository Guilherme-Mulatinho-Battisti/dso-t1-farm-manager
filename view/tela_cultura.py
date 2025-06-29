from view.tela_base import get_layout_opcoes, get_janela, TelaBase, get_layout_listagem
import FreeSimpleGUI as sg


class TelaCultura(TelaBase):
    def tela_opcoes(self) -> int:
        print("-------- CULTURAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cultura")
        print("2 - Alterar Cultura")
        print("3 - Listar Culturas")
        print("4 - Excluir Cultura")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None
        try:
            layout = get_layout_opcoes("Culturas",
                                       ["Incluir Cultura", "Alterar Cultura", "Listar Culturas", "Excluir Cultura"],
                                       "Retornar")

            window = get_janela("Culturas", layout)

            event, values = window.read()

            if event == "Incluir Cultura":
                opcao = 1
            elif event == "Alterar Cultura":
                opcao = 2
            elif event == "Listar Culturas":
                opcao = 3
            elif event == "Excluir Cultura":
                opcao = 4
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

    def pega_dados_cultura(self) -> dict:
        print("-------- DADOS CULTURA ----------")
        nome = input("Nome: ")
        cultura_id = input("ID: ")
        dose_semente = input("Dose de Semente: ")
        dose_fertilizante = input("Dose de Fertilizante: ")
        dose_defensivo = input("Dose de Defensivo: ")
        temp_crescimento = input("Tempo de Crescimento: ")
        num_aplicacao = input("Numero de Aplicações: ")

        return {
            "nome": nome,
            "id": cultura_id,
            "dose_semente": dose_semente,
            "dose_fertilizante": dose_fertilizante,
            "dose_defensivo": dose_defensivo,
            "temp_crescimento": temp_crescimento,
            "num_aplicacao": num_aplicacao,
        }

    def pega_dados_cultura_gui(self) -> dict:
        layout = [
            [sg.Text("DADOS DA CULTURA", font=("Arial", 14, "bold"))],
            [sg.Text("Nome:"), sg.Input(key="-NOME-")],
            [sg.Text("ID:"), sg.Input(key="-ID-")],
            [sg.Text("Dose de Semente:"), sg.Input(key="-DOSE_SEMENTE-")],
            [sg.Text("Dose de Fertilizante:"), sg.Input(key="-DOSE_FERTILIZANTE-")],
            [sg.Text("Dose de Defensivo:"), sg.Input(key="-DOSE_DEFENSIVO-")],
            [sg.Text("Tempo de Crescimento (meses):"), sg.Input(key="-TEMP_CRESCIMENTO-")],
            [sg.Text("Numero de Aplicações:"), sg.Input(key="-NUM_APLICACAO-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window = get_janela("Dados da Cultura", layout)
        dados = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            if event == "-CONFIRMAR-":
                # Validação simples
                if not values["-NOME-"] or not values["-ID-"]:
                    sg.popup_error("Nome e ID são obrigatórios!")
                    continue
                try:
                    dados = {
                        "nome": values["-NOME-"],
                        "id": int(values["-ID-"]),
                        "dose_semente": float(values["-DOSE_SEMENTE-"]),
                        "dose_fertilizante": float(values["-DOSE_FERTILIZANTE-"]),
                        "dose_defensivo": float(values["-DOSE_DEFENSIVO-"]),
                        "temp_crescimento": int(values["-TEMP_CRESCIMENTO-"]),
                        "num_aplicacao": int(values["-NUM_APLICACAO-"])
                    }
                except ValueError:
                    sg.popup_error("Preencha todos os campos corretamente!")
                    continue
                break
        window.close()
        return dados

    def mostra_cultura(self, dados_cultura) -> None:
        print("Nome da Cultura: ", dados_cultura["nome"])
        print("ID da Cultura: ", dados_cultura["id"])
        print("Dose de Semente: ", dados_cultura["dose_semente"])
        print("Dose de Fertilizante: ", dados_cultura["dose_fertilizante"])
        print("Dose de Defensivo: ", dados_cultura["dose_defensivo"])
        print("Tempo de Crescimento: ", dados_cultura["temp_crescimento"])
        print("Numero de Aplicações: ", dados_cultura["num_aplicacao"])
        print("\n")

    def seleciona_cultura(self) -> int:
        return int(input("Digite o ID da cultura que deseja selecionar: "))

    def seleciona_cultura_gui(self, culturas: list) -> int:
        layout = [[sg.Text("Selecione a cultura desejada:", font=("Arial", 14, "bold"))]]
        for cultura in culturas:
            texto = f"ID: {cultura['id']} | Nome: {cultura['nome']}"
            layout.append([
                sg.Text(texto, size=(40, 1)),
                sg.Button("Selecionar", key=f"-SEL-{cultura['id']}-")
            ])
        layout.append([sg.Button("Cancelar", key="-CANCELAR-")])
        window = get_janela("Selecionar Cultura", layout)
        id_cultura = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            for cultura in culturas:
                if event == f"-SEL-{cultura['id']}-":
                    id_cultura = cultura['id']
                    break
            if id_cultura is not None:
                break
        window.close()
        return id_cultura

    def mostra_mensagem(self, msg) -> None:
        print(msg)

    def mostra_mensagem_gui(self, msg):
        sg.popup(msg, title="Mensagem", keep_on_top=True)

    def mostra_culturas_gui(self, culturas: list) -> None:
        if not culturas:
            sg.popup("Nenhuma cultura encontrada. Retornando...")
            return
        linhas = []
        for cultura in culturas:
            linhas.append(
                f"Nome: {cultura['nome']}, ID: {cultura['id']}\nDose de Semente: {cultura['dose_semente']}, "
                f"Dose de Fertilizante: {cultura['dose_fertilizante']}, Dose de Defensivo: {cultura['dose_defensivo']}\n"
                f"Tempo de Crescimento: {cultura['temp_crescimento']}, Numero de Aplicações: {cultura['num_aplicacao']}"
            )
        layout = get_layout_listagem("Culturas", linhas, "Retornar")
        window = get_janela("Culturas", layout)
        window.read()
        window.close()
