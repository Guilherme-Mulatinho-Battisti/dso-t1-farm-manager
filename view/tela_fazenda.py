class TelaFazenda():
    def tela_opcoes(self) -> int:
        print("-------- FAZENDAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Fazenda")
        print("2 - Alterar Fazenda")
        print("3 - Listar Fazendas")
        print("4 - Excluir Fazenda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_fazenda(self) -> dict:
        print("-------- DADOS FAZENDA ----------")
        nome = input("Nome: ")
        area = input("Area Plantada(em m2): ")
        print("--- ENDERECO ---")
        pais = input("Pais: ")
        estado = input("Estado: ")
        cidade = input("Cidade: ")

        return {"nome": nome, "id": id, "dose_semente": dose_semente,
                "dose_fertilizante": dose_fertilizante, "dose_defensivo": dose_defensivo,
                "temp_crescimento": temp_crescimento, "num_aplicacao": num_aplicacao}

    def mostra_fazenda(self, dados_fazenda) -> None:
        print("Nome da Fazenda: ", dados_fazenda["nome"])
        print("ID da Fazenda: ", dados_fazenda["id"])
        print("Dose de Semente: ", dados_fazenda["dose_semente"])
        print("Dose de Fertilizante: ", dados_fazenda["dose_fertilizante"])
        print("Dose de Defensivo: ", dados_fazenda["dose_defensivo"])
        print("Tempo de Crescimento: ", dados_fazenda["temp_crescimento"])
        print("Numero de Aplicações: ", dados_fazenda["num_aplicacao"])
        print("\n")

    def seleciona_fazenda(self) -> int:
        id = input("ID do fazenda que deseja selecionar: ")
        return id

    def mostra_mensagem(self, msg) -> None:
        print(msg)
