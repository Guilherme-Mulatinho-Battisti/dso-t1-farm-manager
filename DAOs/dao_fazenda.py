from DAOs.dao import DAO
from model.fazenda import Fazenda


class FazendaDAO(DAO):
    def __init__(self):
        super().__init__("fazendas.pkl")

    def add(self, fazenda: Fazenda):
        if (fazenda is not None) and isinstance(fazenda, Fazenda) and isinstance(fazenda.id, int):
            super().add(fazenda.id, fazenda)

    def update(self, cultura: Fazenda):
        if (cultura is not None) and isinstance(cultura, Fazenda) and isinstance(cultura.id, int):
            super().update(cultura.id, cultura)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
        return None

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
        return None
