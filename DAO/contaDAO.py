from dao.dao import DAO


class ContaDAO(DAO):
    def __init__(self,):
        super().__init__('contas.pkl')

    def add(self, objeto):
        super().add(objeto.cpf, objeto)