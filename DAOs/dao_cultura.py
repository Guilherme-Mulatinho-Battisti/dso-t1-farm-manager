from DAOs.dao import DAO
from model.cultura import Cultura


class CulturaDAO(DAO):
    def __init__(self):
        super().__init__("culturas.pkl")

    def add(self, cultura: Cultura):
        if ((cultura is not None) and isinstance(cultura, Cultura) and isinstance(cultura.id, int)):
            super().add(cultura.id, cultura)

    def update(self, cultura: Cultura):
        if ((cultura is not None) and isinstance(cultura, Cultura) and isinstance(cultura.id, int)):
            super().update(cultura.id, cultura)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
