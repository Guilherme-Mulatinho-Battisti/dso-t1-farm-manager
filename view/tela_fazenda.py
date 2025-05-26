class TelaFazenda():
    def tela_opcoes(self) -> int:
        print("-------- FAZENDAS ----------")
        print("1 - Incluir Fazenda")
        print("2 - Alterar Fazenda")
        print("3 - Listar Fazendas")
        print("4 - Excluir Fazenda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_gerenciador_fazenda(self) -> int:
        print("-------- GERENCIADOR DE FAZENDA ----------")
        print("1 - Gerenciar Estoque")
        print("2 - Alterar Cultura")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_fazenda(self) -> dict:
        print("-------- DADOS FAZENDA ----------")
        nome = input("Nome: ")
        id = input("ID: ")
        area = input("Area Plantada(em ha): ")

        print("--- ENDERECO ---")
        pais = input("Pais: ")
        estado = input("Estado: ")
        cidade = input("Cidade: ")

        return {"nome": nome, "id": id, "pais": pais,
                "estado": estado, "cidade": cidade,
                "area_plantada": area}

    def mostra_fazenda(self, dados_fazenda: dict) -> None:
        print("Nome da Fazenda: ", dados_fazenda["nome"])
        print("ID da Fazenda: ", dados_fazenda["id"])
        print("Endereço: ", dados_fazenda["endereco"])
        print("Area Plantada: ", dados_fazenda["area_plantada"])
        print("Cultura: ", dados_fazenda["cultura"])
        print("Estoque: ", dados_fazenda["estoque"])
        print("\n")

    def seleciona_fazenda(self) -> int:
        id = input("ID do fazenda que deseja selecionar: ")
        return id

    def mostra_mensagem(self, msg) -> None:
        print(msg)
