class TelaCultura:
    def tela_opcoes(self) -> int:
        print("-------- CULTURAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cultura")
        print("2 - Alterar Cultura")
        print("3 - Listar Culturas")
        print("4 - Excluir Cultura")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_cultura(self) -> dict:
        print("-------- DADOS CULTURA ----------")
        nome = input("Nome: ")
        id = input("ID: ")
        dose_semente = input("Dose de Semente: ")
        dose_fertilizante = input("Dose de Fertilizante: ")
        dose_defensivo = input("Dose de Defensivo: ")
        temp_crescimento = input("Tempo de Crescimento: ")
        num_aplicacao = input("Numero de Aplicações: ")

        return {
            "nome": nome,
            "id": id,
            "dose_semente": dose_semente,
            "dose_fertilizante": dose_fertilizante,
            "dose_defensivo": dose_defensivo,
            "temp_crescimento": temp_crescimento,
            "num_aplicacao": num_aplicacao,
        }

    def mostra_cultura(self, dados_cultura) -> None:
        print("Nome da Cultura: ", dados_cultura["nome"])
        print("ID da Cultura: ", dados_cultura["id"])
        print("Dose de Semente: ", dados_cultura["dose_semente"])
        print("Dose de Fertilizante: ", dados_cultura["dose_fertilizante"])
        print("Dose de Defensivo: ", dados_cultura["dose_defensivo"])
        print("Tempo de Crescimento: ", dados_cultura["temp_crescimento"])
        print("Numero de Aplicações: ", dados_cultura["num_aplicacao"])
        print("\n")

    def seleciona_cultura(self) -> int:
        id = input("ID do cultura que deseja selecionar: ")
        return id

    def mostra_mensagem(self, msg) -> None:
        print(msg)
