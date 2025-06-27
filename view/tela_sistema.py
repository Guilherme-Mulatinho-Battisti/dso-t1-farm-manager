import FreeSimpleGUI as sg
from .tela_base import TelaBase


class TelaSistema(TelaBase):
    def tela_opcoes(self):
        while True:
            print("-------- SisAgro ---------")
            print("Escolha sua opcao")
            print("1 - Insumo")
            print("2 - Cultura")
            print("3 - Fazenda")
            print("4 - Porto")
            print("0 - Finalizar sistema")
            entrada = input("Escolha a opcao: ")

            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 4.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

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
