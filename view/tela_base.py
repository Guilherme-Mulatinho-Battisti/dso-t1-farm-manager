import FreeSimpleGUI as sg


def get_layout_opcoes(titulo, opcoes: list, opcao_retorno):
    layout = [[sg.Text("", size=(1, 1))], [sg.Push(), sg.Text(titulo, font=("Helvetica", 16)), sg.Push()],
              [sg.Text("", size=(1, 1))]]

    for opcao in opcoes:
        layout.append(
            [
                sg.Push(),
                sg.Button(opcao, size=(40, 2), font=("Helvetica", 16)),
                sg.Push(),
            ]
        )
    layout.append([sg.Text("", size=(1, 2))])
    layout.append(
        [
            sg.Push(),
            sg.Button(
                opcao_retorno,
                size=(40, 2),
                font=("Courier New", 15, "bold"),
                button_color=("white", "red"),
            ),
            sg.Push(),
        ]
    )

    return layout


def get_layout_listagem(titulo, lista_itens, opcao_retorno):
    layout = [
        [sg.Push(), sg.Text(titulo, font=("Helvetica", 16)), sg.Push()],
        [
            sg.Multiline(
                '\n'.join(lista_itens),
                size=(80, 20),
                disabled=True,
                font=("Courier New", 14),
            )
        ],
        [
            sg.Push(),
            sg.Button(
                opcao_retorno,
                size=(20, 1),
                font=("Courier New", 14, "bold"),
                button_color=("white", "red"),
            ),
            sg.Push(),
        ],
    ]
    return layout


def get_janela(titulo, layout):
    sg.theme("NeonGreen1")
    return sg.Window(titulo, layout, size=(800, 500), resizable=True, finalize=True)


class TelaBase:

    def tela_opcoes(self):
        raise NotImplementedError("Método tela_opcoes deve ser implementado na subclasse.")
