from controller.controlador_insumo import ControladorInsumo
from model.insumo import DefensInsumoivo

  def tela_opcoes(self):
    print("-------- LIVROS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Livro")
    print("2 - Alterar Livro")
    print("3 - Listar Livro")
    print("4 - Excluir Livro")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

def menu_insumos():
    ctrl = ControladorInsumo()

    print("Cadastro de Defensivo")
    nome = input("Nome: ")
    valor = float(input("Valor por litro: "))
    funcao = input("Função (Herbicida, Fungicida, etc): ")

    defensivo = Defensivo(nome, valor, funcao)
    ctrl.adicionar_insumo(defensivo)

    print("\nInsumos cadastrados:")
    for insumo in ctrl.listar_insumos():
        print(f"- {insumo.nome}: R$ {insumo.valor} ({insumo.funcao})")
