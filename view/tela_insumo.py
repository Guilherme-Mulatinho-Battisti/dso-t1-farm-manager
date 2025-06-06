class TelaInsumo():
    def tela_opcoes(self):
        print("\n")
        while True:
            print("-------- INSUMOS ----------")
            print("Escolha a opcao")
            print("1 - Incluir Insumo")
            print("2 - Alterar Insumo")
            print("3 - Listar Insumo")
            print("4 - Excluir Insumo")
            print("0 - Retornar")

            entrada = input("Escolha a opcao: ")

            # Verifica se a entrada é um número e se está dentro do intervalo esperado
            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 a 4.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

    def tela_opcoes_insumos(self):
        print("\n")
        while True:
            print("-------- TIPOS DE INSUMO ----------")
            print("1 - Fertilizante")
            print("2 - Defensivo")
            print("3 - Semente")
            print("4 - Implemento")
            print("0 - Retornar")

            entrada = input("Escolha a opcao: ")
            # Verifica se a entrada é um número e se está dentro do intervalo esperado
            try:
                opcao = int(entrada)
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número de 0 a 4.\n")
            except ValueError:
                print("Entrada inválida. Digite apenas números.\n")

    def pega_dados_insumo(self, tipo_insumo=None):
        print("-------- DADOS DO INSUMO ----------")
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            print("Nome não pode ser vazio.")

        while True:
            id = input("ID: ").strip()
            if not id:
                print("Id não pode ser vazio.")
                continue
            if not id.isdigit():
                print("Id deve ser um número inteiro.")
                continue
            id = int(id)
            break

        while True:
            valor = input("Valor: ").strip()
            if not valor:
                print("Valor não pode ser vazio.")
                continue
            if not isinstance(valor, (int, float)):
                print("Valor deve ser um número float.")
                continue
            valor = float(valor)
            break

        # FERTILIZANTES
        if tipo_insumo == 1:
            while True:
                fonte = input("Fonte (Organico ou Quimico): ").strip()
                if fonte:
                    break
                print("Fonte não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "fonte": fonte}

        # DEFENSIVOS
        if tipo_insumo == 2:
            while True:
                funcao = input("Função (Herbicida, Fungicida, Inseticida ou Acaricida): ").strip()
                if funcao:
                    break
                print("Funcao não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "funcao": funcao}

        # SEMENTES
        if tipo_insumo == 3:
            while True:
                cultura = input("Cultura (Soja, Milho, Trigo ou Algodão): ").strip()
                if cultura:
                    break
                print("cultura não pode ser vazio.")
            while True:
                tecnologia = input("Tecnologia (Transgenica ou Nao Transgenica): ").strip()
                if tecnologia:
                    break
                print("Tecnologia não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "cultura": cultura, "tecnologia": tecnologia}

        # IMPLEMENTOS
        if tipo_insumo == 4:
            while True:
                processo = input("Processo (Pantio ou Colheita): ").strip()
                if processo:
                    break
                print("Processo não pode ser vazio.")
            while True:
                tipo = input("Tipo (Manual ou Mecanico): ").strip()
                if tipo:
                    break
                print("Tipo não pode ser vazio.")
            return {"nome": nome, "id": id, "valor": valor, "processo": processo, "tipo": tipo}

    def mostra_insumo(self, dados_insumo: dict):
        for key, value in dados_insumo.items():
            print(f"{key.upper()}: {value}")

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
