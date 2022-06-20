from datetime import datetime
from View.telalogs import TelaLog

class Log:
    def __init__(self):
        self.__log = []
        self.__tela_log = TelaLog()

    @property
    def log(self):
        return self.__log

    def incluir_log(self, string: str):
        self.__log.append(datetime.now().strftime('%d/%m/%Y %H:%M: ') + string)

    @property
    def tela_log(self):
        return self.__tela_log
