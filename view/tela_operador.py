from view.tela_base import get_layout_opcoes, get_janela, TelaBase


class TelaOperador(TelaBase):
    def tela_opcoes(self):
        print("\n")
        while True:
            print("-------- INSUMOS ----------")
            print("Escolha a opcao")
            print("1 - Plantar")
            print("2 - Colher")
            print("3 - Aplicar Insumo")
            print("0 - Retornar")

            entrada = input("Escolha a opcao: ")

            # Verifica se a entrada é um número e se está dentro do intervalo esperado
            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 a 3.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

    def tela_opcoes_gui(self):
        window, opcao = None, None

        try:
            layout = get_layout_opcoes(
                titulo="Operador",
                opcoes=["Plantar", "Colher", "Aplicar Insumo"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Operador", layout)
            event, values = window.read()

            if event == "Plantar":
                opcao = 1
            elif event == "Colher":
                opcao = 2
            elif event == "Aplicar Insumo":
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

    def seleciona_insumo(self):
        entrada = input("Nome do insumo que deseja selecionar: ").strip()
        return entrada

    def mostra_mensagem(self, msg):
        print(msg)
