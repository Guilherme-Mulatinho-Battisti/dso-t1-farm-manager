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
            [sg.Text("DADOS DA CULTURA", font=("Arial", 16, "bold"), justification="center", expand_x=True)],
            [sg.HorizontalSeparator()],
            [sg.Text("Nome:", size=(20, 1)), sg.Input(key="-NOME-", size=(30, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("ID:", size=(20, 1)), sg.Input(key="-ID-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("Dose de Semente:", size=(20, 1)), sg.Input(key="-DOSE_SEMENTE-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("Dose de Fertilizante:", size=(20, 1)), sg.Input(key="-DOSE_FERTILIZANTE-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("Dose de Defensivo:", size=(20, 1)), sg.Input(key="-DOSE_DEFENSIVO-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("Tempo de Crescimento (meses):", size=(20, 1)), sg.Input(key="-TEMP_CRESCIMENTO-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.Text("Numero de Aplicações:", size=(20, 1)), sg.Input(key="-NUM_APLICACAO-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
            [sg.HorizontalSeparator()],
            [sg.Push(), sg.Button("Confirmar", key="-CONFIRMAR-", size=(12, 1), button_color=("white", "#00796B")),
             sg.Button("Cancelar", key="-CANCELAR-", size=(12, 1), button_color=("white", "#B71C1C")), sg.Push()]
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

    def seleciona_cultura_gui(self, culturas: list) -> int | None:
        if not culturas:
            sg.popup("Nenhuma cultura cadastrada. Retornando...")
            return None
            
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
        
        layout = [
            [sg.Text("LISTAGEM DE CULTURAS", font=("Arial", 16, "bold"), justification="center", expand_x=True, text_color="#2E7D32")],
            [sg.HorizontalSeparator()]
        ]
        
        # Lista simples e organizada
        for i, cultura in enumerate(culturas):
            
            cultura_info = [
                [sg.Frame("", [
                    [sg.Text(f"🌱 {cultura['nome']}", font=("Arial", 12, "bold"), text_color="#2E7D32"),
                     sg.Push(), 
                     sg.Text(f"ID: {cultura['id']}", font=("Arial", 10), text_color="#666666")],
                    [sg.Text(f"Dose de Semente: {cultura['dose_semente']:.2f} kg/ha", font=("Arial", 10))],
                    [sg.Text(f"Dose de Fertilizante: {cultura['dose_fertilizante']:.2f} kg/ha", font=("Arial", 10))],
                    [sg.Text(f"Dose de Defensivo: {cultura['dose_defensivo']:.2f} L/ha", font=("Arial", 10))],
                    [sg.Text(f"Tempo de Crescimento: {cultura['temp_crescimento']} meses", font=("Arial", 10))],
                    [sg.Text(f"Número de Aplicações: {cultura['num_aplicacao']}x", font=("Arial", 10))]
                ], border_width=1, relief=sg.RELIEF_FLAT, expand_x=True)]
            ]
            
            layout.extend(cultura_info)
        
        layout.extend([
            [sg.HorizontalSeparator()],
            [sg.Push(), sg.Button("Retornar", size=(12, 1), button_color=("white", "#4CAF50")), sg.Push()]
        ])
        
        window = get_janela("Culturas", layout)
        window.read()
        window.close()
