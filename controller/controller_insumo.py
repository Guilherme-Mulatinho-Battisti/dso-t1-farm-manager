from app.model.insumo import Defensivo, Fertilizante, Implemento, Semente

class InsumoController:
    def __init__(self):
        self.insumos = []

    def adicionar_insumo(self, insumo):
        self.insumos.append(insumo)

    def listar_insumos(self):
        return self.insumos

    def buscar_por_nome(self, nome: str):
        return [i for i in self.insumos if i.nome == nome]
