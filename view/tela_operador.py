class TelaOperador():
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

    def seleciona_insumo(self):
        while True:
            entrada = input("Código do insumo que deseja selecionar: ").strip()
            if not entrada:
                print("Id não pode ser vazio.")
                continue
            if not entrada.isdigit():
                print("Id deve ser um número inteiro.")
                continue
            return int(entrada)

    def mostra_mensagem(self, msg):
        print(msg)
