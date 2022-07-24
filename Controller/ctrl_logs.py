from datetime import datetime
from view.tela_logs import TelaLog
#from dao.logDAO import LogDAO

class Log:
    def __init__(self):
        self.__log = []
        self.__tela_log = TelaLog()
        self.__log_rep = []

    @property
    def log(self):
        return self.__log

    @property
    def tela_log(self):
        return self.__tela_log

    def incluir_log(self, string: str, usuario=None, modo=None):
        if modo == 'Sistema':
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S  :  ')
            acao = string.split(': ')[1]
            log = data_hora + f'##{usuario.empresa}/{usuario.cpf}## ' + acao
            if string not in self.__log_rep:
                self.__log.append(log)
                self.__log_rep.append(string)
        elif string not in self.log:
            self.log.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S  :  ') + string)
