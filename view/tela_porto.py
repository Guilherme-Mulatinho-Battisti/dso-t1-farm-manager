class TelaPorto():
    def tela_opcoes(self) -> int:
        while True:
            print("-------- PORTOS ----------")
            print("1 - Incluir Porto")
            print("2 - Gerenciar Porto")
            print("3 - Alterar Porto")
            print("4 - Listar Portos")
            print("5 - Excluir Porto")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                else:
                    print("Opção fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def pega_dados_porto(self) -> dict:
        print("-------- DADOS PORTO ----------")

        nome = input("Nome: ")
        while not isinstance(nome, str) or nome.strip() == "":
            nome = input("Nome inválido. Digite novamente: ")

        while True:
            try:
                id = int(input("ID (número inteiro): "))
                break
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

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
        }

    def mostra_porto(self, dados_porto: dict) -> None:
        print("Nome da Porto: ", dados_porto["nome"])
        print("ID da Porto: ", dados_porto["id"])
        print("Endereço: ", dados_porto["endereco"])
        print("Estoque: ", dados_porto["estoque"])
        print("\n")

    def seleciona_porto(self) -> int:
        while True:
            try:
                id = int(input("ID do porto que deseja selecionar: "))
                return id
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def mostra_mensagem(self, msg) -> None:
        print(msg)
