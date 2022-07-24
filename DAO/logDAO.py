from DAO.dao import DAO


class LogDAO(DAO):
    def __init__(self,):
        self.lognumero = 0
        super().__init__('logs.pkl')

    def add(self, objeto):
        super().add(self.log, objeto)
        self.log += 1
