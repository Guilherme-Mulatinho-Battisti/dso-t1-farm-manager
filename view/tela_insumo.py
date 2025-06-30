from view.tela_base import get_layout_opcoes, get_janela, TelaBase, get_layout_listagem
import FreeSimpleGUI as sg


class TelaInsumo(TelaBase):

    def tela_opcoes_gui(self):
        window, opcao = None, None

        try:

            layout = get_layout_opcoes("Insumos",
                                       opcoes=["Incluir Insumo", "Alterar Insumo", "Listar Insumo", "Excluir Insumo"],
                                       opcao_retorno="Retornar")

            window = get_janela("Insumos", layout)
            event, values = window.read()

            if event == "Incluir Insumo":
                opcao = 1
            elif event == "Alterar Insumo":
                opcao = 2
            elif event == "Listar Insumo":
                opcao = 3
            elif event == "Excluir Insumo":
                opcao = 4
            else:
                print("Retornado!")
                opcao = 0
        except ValueError as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e
        finally:
            if window is not None:
                window.close()
            if opcao is None:
                print("Nenhuma opção selecionada. Retornando...")
                opcao = 0

        return opcao


    def tela_opcoes_insumos_gui(self):
        window, opcao = None, None

        try:
            layout = get_layout_opcoes("Que insumos voce deseja incluir?",
                                       opcoes=["Fertilizante", "Defensivo", "Semente", "Implemento"],
                                       opcao_retorno="Cancelar")

            window = get_janela("Tipos de Insumo", layout)
            event, values = window.read()

            if event == "Fertilizante":
                opcao = 1
            elif event == "Defensivo":
                opcao = 2
            elif event == "Semente":
                opcao = 3
            elif event == "Implemento":
                opcao = 4
            else:
                print("Retornado!")
                opcao = 0
        except ValueError as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e
        finally:
            if window is not None:
                window.close()
            if opcao is None:
                print("Nenhuma opção selecionada. Retornando...")
                opcao = 0

        return opcao

    def mostra_insumo_gui(self, dados_insumo: list) -> None:
        linhas = []

        for insumo in dados_insumo:
            for k, v in insumo.items():
                linhas.append(f"{k.capitalize()}: {v}")
            linhas.append("")
        layout = get_layout_listagem("Detalhes do Insumo",
                                     linhas,
                                     opcao_retorno="Retornar")

        window = get_janela("Insumos", layout)
        window.read()
        window.close()

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem", keep_on_top=True)

    def pega_dados_insumo_gui(self, tipo_insumo=None):
        window, dados = None, None

        try:
            # Campos comuns para todos os tipos de insumo
            layout_comum = [
                [sg.Text("DADOS DO INSUMO", font=("Arial", 16, "bold"), justification="center", expand_x=True)],
                [sg.HorizontalSeparator()],
                [sg.Text("Nome:", size=(12, 1)), sg.Input(key="-NOME-", size=(30, 1)), sg.Push(), sg.Text("*", text_color="red")],
                [sg.Text("ID:", size=(12, 1)), sg.Input(key="-ID-", size=(10, 1)), sg.Push(), sg.Text("*", text_color="red")],
                [sg.Text("Valor:", size=(12, 1)), sg.Input(key="-VALOR-", size=(15, 1)), sg.Push(), sg.Text("*", text_color="red")],
            ]

            layout_especifico = []

            if tipo_insumo == 1:  # FERTILIZANTES
                layout_especifico = [
                    [sg.Text("Fonte:", size=(12, 1)), sg.Combo(["Organico", "Quimico"], key="-FONTE-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")]
                ]
            elif tipo_insumo == 2:  # DEFENSIVOS
                layout_especifico = [
                    [sg.Text("Função:", size=(12, 1)), sg.Combo(["Herbicida", "Fungicida", "Inseticida", "Acaricida"],
                                                      key="-FUNCAO-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")]
                ]
            elif tipo_insumo == 3:  # SEMENTES
                layout_especifico = [
                    [sg.Text("Cultura:", size=(12, 1)), sg.Combo(["Soja", "Milho", "Trigo", "Algodão"],
                                                   key="-CULTURA-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")],
                    [sg.Text("Tecnologia:", size=(12, 1)), sg.Combo(["Transgenica", "Nao Transgenica"],
                                                      key="-TECNOLOGIA-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")]
                ]
            elif tipo_insumo == 4:  # IMPLEMENTOS
                layout_especifico = [
                    [sg.Text("Processo:", size=(12, 1)), sg.Combo(["Plantio", "Colheita"],
                                                    key="-PROCESSO-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")],
                    [sg.Text("Tipo:", size=(12, 1)), sg.Combo(["Manual", "Mecanico"],
                                                key="-TIPO-", size=(20, 1)), sg.Push(), sg.Text("*", text_color="red")]
                ]

            layout = layout_comum + layout_especifico + [
                [sg.HorizontalSeparator()],
                [sg.Push(), sg.Button("Confirmar", key="-CONFIRMAR-", size=(12, 1), button_color=("white", "#00796B")),
                 sg.Button("Cancelar", key="-CANCELAR-", size=(12, 1), button_color=("white", "#B71C1C")), sg.Push()]
            ]

            window = get_janela("Dados do Insumo", layout)

            if window is None:
                return None

            while True:
                try:
                    event, values = window.read()
                except Exception:
                    break

                if event in (sg.WIN_CLOSED, "-CANCELAR-", None):
                    break

                if event == "-CONFIRMAR-":
                    # Validação dos campos comuns
                    nome = values["-NOME-"].strip()
                    if not nome:
                        sg.popup_error("Nome não pode ser vazio!")
                        continue

                    id_str = values["-ID-"].strip()
                    if not id_str:
                        sg.popup_error("ID não pode ser vazio!")
                        continue
                    if not id_str.isdigit():
                        sg.popup_error("ID deve ser um número inteiro!")
                        continue
                    id_insumo = int(id_str)

                    valor_str = values["-VALOR-"].strip()
                    if not valor_str:
                        sg.popup_error("Valor não pode ser vazio!")
                        continue
                    try:
                        valor = float(valor_str)
                    except ValueError:
                        sg.popup_error("Valor deve ser um número!")
                        continue

                    # Dados básicos
                    dados = {"nome": nome, "id": id_insumo, "valor": valor}

                    # Validação e adição de campos específicos
                    if tipo_insumo == 1:  # FERTILIZANTES
                        fonte = values["-FONTE-"]
                        if not fonte:
                            sg.popup_error("Fonte não pode ser vazia!")
                            continue
                        dados["fonte"] = fonte

                    elif tipo_insumo == 2:  # DEFENSIVOS
                        funcao = values["-FUNCAO-"]
                        if not funcao:
                            sg.popup_error("Função não pode ser vazia!")
                            continue
                        dados["funcao"] = funcao

                    elif tipo_insumo == 3:  # SEMENTES
                        cultura = values["-CULTURA-"]
                        tecnologia = values["-TECNOLOGIA-"]
                        if not cultura:
                            sg.popup_error("Cultura não pode ser vazia!")
                            continue
                        if not tecnologia:
                            sg.popup_error("Tecnologia não pode ser vazia!")
                            continue
                        dados["cultura"] = cultura
                        dados["tecnologia"] = tecnologia

                    elif tipo_insumo == 4:  # IMPLEMENTOS
                        processo = values["-PROCESSO-"]
                        tipo = values["-TIPO-"]
                        if not processo:
                            sg.popup_error("Processo não pode ser vazio!")
                            continue
                        if not tipo:
                            sg.popup_error("Tipo não pode ser vazio!")
                            continue
                        dados["processo"] = processo
                        dados["tipo"] = tipo

                    break

        except Exception as e:
            sg.popup_error(f"Erro ao processar dados: {e}")
            dados = None
        finally:
            if window is not None:
                window.close()

        return dados

    def seleciona_insumo_gui(self, dados_insumos):
        layout = [
            [sg.Text("Selecione o insumo desejado:", font=("Arial", 14, "bold"))],
        ]
        for insumo in dados_insumos:
            texto = f"ID: {insumo.get('id', '')} | Nome: {insumo.get('nome', '')} | Valor: {insumo.get('valor', '')}"
            layout.append([
                sg.Text(texto, size=(60, 1), font=("Courier New", 12)),
                sg.Button("Selecionar", key=f"-SEL-{insumo.get('id', '')}-")
            ])
        layout.append([sg.Button("Cancelar", key="-CANCELAR-")])
        window = get_janela("Selecionar Insumo", layout)
        id_insumo = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            for insumo in dados_insumos:
                if event == f"-SEL-{insumo.get('id', '')}-":
                    id_insumo = insumo.get('id', None)
                    break
            if id_insumo is not None:
                break
        window.close()
        return id_insumo
