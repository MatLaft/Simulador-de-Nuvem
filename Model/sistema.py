from Controller.ctrlconta import *
from View.telasistema import *

class Sistema:
    def __init__(self):
        self.controlador_conta = CtrlConta()
        self.__usuario_ativo = None
        self.__servidores = []
        self.__tela_sistema = TelaSistema()

    @property
    def usuario_ativo(self):
        return self.__usuario_ativo

    @property
    def servidores(self):
        return self.__servidores

    def logar(self):
        while True:
            self.__usuario_ativo = self.controlador_conta.logar()
            if self.usuario_ativo:
                self.__tela_sistema.tela_login(1)
                break
            voltar = self.__tela_sistema.tela_login()
            if voltar == '0':
                break

    def menu_inical(self):
        switcher = {1: self.logar, 2:self.controlador_conta.cadastrar_usuario()}
        opcao = self.__tela_sistema.tela_menu_inicial()
        if opcao == 0:
            return
        switcher[int(opcao)]()
