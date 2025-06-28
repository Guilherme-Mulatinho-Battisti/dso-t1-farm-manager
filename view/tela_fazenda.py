from view.tela_base import get_layout, TelaBase, get_janela


class TelaFazenda(TelaBase):
    def tela_opcoes(self) -> int:
        while True:
            print("-------- FAZENDAS ----------")
            print("1 - Incluir Fazenda")
            print("2 - Gerenciar Fazenda")
            print("3 - Alterar Fazenda")
            print("4 - Listar Fazendas")
            print("5 - Excluir Fazenda")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None

        try:
            layout = get_layout(
                titulo="Fazendas",
                opcoes=["Incluir Fazenda", "Gerenciar Fazenda", "Alterar Fazenda", "Listar Fazendas",
                        "Excluir Fazenda"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Fazendas", layout)
            event, values = window.read()

            if event == "Incluir Fazenda":
                opcao = 1
            elif event == "Gerenciar Fazenda":
                opcao = 2
            elif event == "Alterar Fazenda":
                opcao = 3
            elif event == "Listar Fazendas":
                opcao = 4
            elif event == "Excluir Fazenda":
                opcao = 5
            else:
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e

        finally:
            if window is not None:
                window.close()

        return opcao

    def tela_gerenciador_fazenda(self) -> int:
        while True:
            print("-------- GERENCIADOR DE FAZENDA ----------")
            print("1 - Gerenciar Estoque")
            print("2 - Alterar Cultura")
            print("3 - Plantar")
            print("4 - Colher")
            print("5 - Aplicar Defensivo")
            print("6 - Aplicar Fertilizante")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5, 6]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def pega_dados_fazenda(self) -> dict:
        print("-------- DADOS FAZENDA ----------")

        nome = input("Nome: ")
        while not isinstance(nome, str) or nome.strip() == "":
            nome = input("Nome inválido. Digite novamente: ")

        while True:
            try:
                id = int(input("ID (número inteiro): "))
                break
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

        while True:
            try:
                area = int(input("Área Plantada (em ha - número inteiro): "))
                break
            except ValueError:
                print("Área inválida. Digite um número inteiro.")

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
            "area_plantada": area,
        }

    def mostra_fazenda(self, dados_fazenda: dict) -> None:
        print("Nome da Fazenda: ", dados_fazenda["nome"])
        print("ID da Fazenda: ", dados_fazenda["id"])
        print("Endereço: ", dados_fazenda["endereco"])
        print("Area Plantada: ", dados_fazenda["area_plantada"])
        print("Cultura: ", dados_fazenda["cultura"])
        print("Estoque: ", dados_fazenda["estoque"])
        print("\n")

    def seleciona_fazenda(self) -> int:
        while True:
            try:
                id = int(input("ID do fazenda que deseja selecionar: "))
                return id
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def mostra_mensagem(self, msg) -> None:
        print(msg)
