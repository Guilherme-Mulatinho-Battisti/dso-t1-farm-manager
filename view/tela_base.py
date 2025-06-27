import FreeSimpleGUI as sg


class TelaBase:
    def get_layout(self, titulo, opcoes: list, opcao_retorno):
        conteudo = [[sg.Push(), sg.Text(titulo, font=("Helvetica", 16)), sg.Push()]]
        for opcao in opcoes:
            conteudo.append(
                [
                    sg.Push(),
                    sg.Button(opcao, size=(50, 1), font=("Helvetica", 16)),
                    sg.Push(),
                ]
            )
        conteudo.append(
            [
                sg.Push(),
                sg.Button(
                    opcao_retorno,
                    size=(50, 1),
                    font=("Courier New", 15, "bold"),
                    button_color=("white", "red"),
                ),
                sg.Push(),
            ]
        )

        return conteudo

    def get_janela(self, titulo, layout):
        sg.theme("NeonGreen1")
        return sg.Window(titulo, layout, size=(600, 300), resizable=True, finalize=True)
