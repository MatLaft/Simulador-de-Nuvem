from datetime import datetime
from dao.logDAO import LogDAO
from view.tela_geral import Tela


class Log:
    __isinstance = None

    def __init__(self):
        self.__log = LogDAO()

    def __new__(cls):
        if Log.__isinstance is None:
            Log.__isinstance = object.__new__(cls)
        return Log.__isinstance

    @property
    def log(self):
        return self.__log.cache.keys()

    def incluir_log(self, string: str, usuario=None):
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S  :  ')
        if usuario is not None:
            log = data_hora + f'##{usuario.empresa}/{usuario.cpf}## ' + string
        else:
            log = data_hora + string
        self.__log.add(log, 1)
