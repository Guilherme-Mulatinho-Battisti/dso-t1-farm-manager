class TelaSistema:
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisAgro ---------")
        print("Escolha sua opcao")
        print("1 - Insumo")
        print("2 - Cultura")
        print("3 - Fazenda")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
