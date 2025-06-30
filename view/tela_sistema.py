import FreeSimpleGUI as sg
from .tela_base import TelaBase


class TelaSistema(TelaBase):

    def tela_opcoes_gui(self):
        sg.theme("NeonGreen1")

        layout = super().get_layout(
            titulo="Escolha uma opção",
            opcoes=["Insumo", "Cultura", "Fazenda", "Porto"],
            opcao_retorno="Finalizar sistema",
        )

        while True:
            window = super().get_janela("SisAgro", layout)

            event, values = window.read()
            opcao = None
            if event == sg.WIN_CLOSED or event == "Finalizar sistema":
                print("Sistema finalizada com sucesso!")
                opcao = 0
            elif event == "Insumo":
                opcao = 1
            elif event == "Cultura":
                opcao = 2
            elif event == "Fazenda":
                opcao = 3
            elif event == "Porto":
                opcao = 4

            window.close()
            return opcao
