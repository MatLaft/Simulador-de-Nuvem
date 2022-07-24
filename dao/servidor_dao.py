from dao.dao import DAO
from model.servidor import Servidor


class ServidorDao(DAO):
    def __init__(self):
        super().__init__('servidor.pkl')

    def add(self, servidor: Servidor):
        super().add(servidor.nome_empresa, servidor)

    def remove(self, key):
        return super().remove(key)

    def get(self, key):
        return super().get(key)

    def get_all(self):
        return super().get_all()
