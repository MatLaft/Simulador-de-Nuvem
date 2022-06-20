from datetime import datetime

class Log:
    def __init__(self):
        self.__log = []

    @property
    def log(self):
        return self.__log

    def incluir_log(self, string: str):
        self.__log.append(datetime.now().strftime('%d/%m/%Y %H:%M: ') + string)
