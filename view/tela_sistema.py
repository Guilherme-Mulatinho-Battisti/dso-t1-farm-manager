class TelaSistema:
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
