from dao.dao import DAO


class LogDAO(DAO):
    def __init__(self,):
        super().__init__('log.pkl')

    def add(self, log, log_rep):
        super().add(log, log_rep)
