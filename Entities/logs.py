from datetime import datetime
from View.telalogs import TelaLog

class Log:
    def __init__(self):
        self.__log = {}
        self.__tela_log = TelaLog()
        self.__id = 0

    @property
    def log(self):
        return list(self.__log.values())

    def incluir_log(self, string: str):
        if self.__id not in self.__log.keys():
            self.__log[self.__id]=(datetime.now().strftime('%d/%m/%Y %H:%M: ') + string)
            self.__id += 1

    @property
    def tela_log(self):
        return self.__tela_log
