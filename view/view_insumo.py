from app.controller.controller_insumo import InsumoController
from app.model.insumo import Defensivo

def menu_insumos():
    ctrl = InsumoController()

    print("Cadastro de Defensivo")
    nome = input("Nome: ")
    valor = float(input("Valor por litro: "))
    funcao = input("Função (Herbicida, Fungicida, etc): ")

    defensivo = Defensivo(nome, valor, funcao)
    ctrl.adicionar_insumo(defensivo)

    print("\nInsumos cadastrados:")
    for insumo in ctrl.listar_insumos():
        print(f"- {insumo.nome}: R$ {insumo.valor} ({insumo.funcao})")
