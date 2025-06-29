from view.tela_base import get_layout_opcoes, get_janela, TelaBase, get_layout_listagem
import FreeSimpleGUI as sg


class TelaInsumo(TelaBase):
    def tela_opcoes(self):
        print("\n")
        while True:
            print("-------- INSUMOS ----------")
            print("Escolha a opcao")
            print("1 - Incluir Insumo")
            print("2 - Alterar Insumo")
            print("3 - Listar Insumo")
            print("4 - Excluir Insumo")
            print("0 - Retornar")

            entrada = input("Escolha a opcao: ")

            # Verifica se a entrada é um número e se está dentro do intervalo esperado
            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 a 4.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

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

    def tela_opcoes_insumos(self):
        print("\n")
        while True:
            print("-------- TIPOS DE INSUMO ----------")
            print("1 - Fertilizante")
            print("2 - Defensivo")
            print("3 - Semente")
            print("4 - Implemento")
            print("0 - Retornar")

            entrada = input("Escolha a opcao: ")
            # Verifica se a entrada é um número e se está dentro do intervalo esperado
            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 a 4.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

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

    def pega_dados_insumo(self, tipo_insumo=None):
        print("-------- DADOS DO INSUMO ----------")
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            print("Nome não pode ser vazio.")

        while True:
            id = input("ID: ").strip()
            if not id:
                print("Id não pode ser vazio.")
                continue
            if not id.isdigit():
                print("Id deve ser um número inteiro.")
                continue
            id = int(id)
            break

        while True:
            valor = input("Valor: ").strip()
            if not valor:
                print("Valor não pode ser vazio.")
                continue
            if not isinstance(valor, (int, float)):
                print("Valor deve ser um número float.")
                continue
            valor = float(valor)
            break

        # FERTILIZANTES
        if tipo_insumo == 1:
            while True:
                fonte = input("Fonte (Organico ou Quimico): ").strip()
                if fonte:
                    break
                print("Fonte não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "fonte": fonte}

        # DEFENSIVOS
        if tipo_insumo == 2:
            while True:
                funcao = input(
                    "Função (Herbicida, Fungicida, Inseticida ou Acaricida): "
                ).strip()
                if funcao:
                    break
                print("Funcao não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "funcao": funcao}

        # SEMENTES
        if tipo_insumo == 3:
            while True:
                cultura = input("Cultura (Soja, Milho, Trigo ou Algodão): ").strip()
                if cultura:
                    break
                print("cultura não pode ser vazio.")
            while True:
                tecnologia = input(
                    "Tecnologia (Transgenica ou Nao Transgenica): "
                ).strip()
                if tecnologia:
                    break
                print("Tecnologia não pode ser vazio.")
            return {
                "nome": nome,
                "id": id,
                "valor": valor,
                "cultura": cultura,
                "tecnologia": tecnologia,
            }

        # IMPLEMENTOS
        if tipo_insumo == 4:
            while True:
                processo = input("Processo (Pantio ou Colheita): ").strip()
                if processo:
                    break
                print("Processo não pode ser vazio.")
            while True:
                tipo = input("Tipo (Manual ou Mecanico): ").strip()
                if tipo:
                    break
                print("Tipo não pode ser vazio.")
            return {
                "nome": nome,
                "id": id,
                "valor": valor,
                "processo": processo,
                "tipo": tipo,
            }

        return None

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
                [sg.Text("DADOS DO INSUMO", font=("Arial", 14, "bold"))],
                [sg.Text("Nome:"), sg.Input(key="-NOME-", size=(30, 1))],
                [sg.Text("ID:"), sg.Input(key="-ID-", size=(10, 1))],
                [sg.Text("Valor:"), sg.Input(key="-VALOR-", size=(15, 1))],
            ]

            layout_especifico = []

            if tipo_insumo == 1:  # FERTILIZANTES
                layout_especifico = [
                    [sg.Text("Fonte:"), sg.Combo(["Organico", "Quimico"], key="-FONTE-", size=(20, 1))]
                ]
            elif tipo_insumo == 2:  # DEFENSIVOS
                layout_especifico = [
                    [sg.Text("Função:"), sg.Combo(["Herbicida", "Fungicida", "Inseticida", "Acaricida"],
                                                  key="-FUNCAO-", size=(20, 1))]
                ]
            elif tipo_insumo == 3:  # SEMENTES
                layout_especifico = [
                    [sg.Text("Cultura:"), sg.Combo(["Soja", "Milho", "Trigo", "Algodão"],
                                                   key="-CULTURA-", size=(20, 1))],
                    [sg.Text("Tecnologia:"), sg.Combo(["Transgenica", "Nao Transgenica"],
                                                      key="-TECNOLOGIA-", size=(20, 1))]
                ]
            elif tipo_insumo == 4:  # IMPLEMENTOS
                layout_especifico = [
                    [sg.Text("Processo:"), sg.Combo(["Plantio", "Colheita"],
                                                    key="-PROCESSO-", size=(20, 1))],
                    [sg.Text("Tipo:"), sg.Combo(["Manual", "Mecanico"],
                                                key="-TIPO-", size=(20, 1))]
                ]

            layout = layout_comum + layout_especifico + [
                [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
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
