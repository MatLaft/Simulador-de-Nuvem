import time

class Log:
    def __init__(self):
        self.__log = []

    @property
    def log(self):
        return self.__log

    def incluir_log(self, string: str):
        self.__log.append(time.ctime()+': ' +string)
