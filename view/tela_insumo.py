class TelaInsumo():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- INSUMOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Insumo")
        print("2 - Alterar Insumo")
        print("3 - Listar Insumo")
        print("4 - Excluir Insumo")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_insumos(self):
        print("-------- INSUMOS ----------")
        print("Escolha a opcao")
        print("1 - Fertilizante")
        print("2 - Defensivo")
        print("3 - Semente")
        print("4 - Implemento")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_insumo(self):
        print("-------- DADOS LIVRO ----------")
        titulo = input("Titulo: ")
        codigo = input("Codigo: ")

        return {"titulo": titulo, "codigo": codigo}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_insumo(self, dados_insumo):
        print("TITULO DO LIVRO: ", dados_insumo["titulo"])
        print("CODIGO DO LIVRO: ", dados_insumo["codigo"])
        print("\n")

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_insumo(self):
        codigo = input("Código do insumo que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)