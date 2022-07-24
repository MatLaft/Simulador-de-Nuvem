from dao.dao import DAO
from model.diretorio import Diretorio


class DiretorioDao(DAO):
    def __init__(self):
        super().__init__('diretorio.pkl')

    def add(self, diretorio: Diretorio):
        super().add(diretorio.usuario.cpf, diretorio)

    def remove(self, key):
        return super().remove(key)

    def get(self, key):
        return super().get(key)

    def get_all(self):
        return super().get_all()