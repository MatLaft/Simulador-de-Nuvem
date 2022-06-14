from Controller.ctrlconta import *
from View.telasistema import *


class Sistema:
    def __init__(self):
        self.__controlador_conta = CtrlConta()
        self.__usuario_ativo = None
        self.__servidores = []
        self.__tela_sistema = TelaSistema()
        self.diretorio = None
        self.cota = None

    @property
    def usuario_ativo(self):
        return self.__usuario_ativo

    @property
    def servidores(self):
        return self.__servidores

    def logar(self):
        while True:
            self.__usuario_ativo = self.__controlador_conta.logar()
            if self.usuario_ativo:
                self.__tela_sistema.tela_login(1)
                break
            voltar = self.__tela_sistema.tela_login()
            if voltar == '0':
                break

    def menu_inical(self):
        switcher = {1: self.logar, 2: self.__controlador_conta.cadastrar_usuario}
        while self.__usuario_ativo is None:
            opcao = self.__tela_sistema.tela_menu_inicial()
            if opcao == 0:
                return
            switcher[int(opcao)]()

    def menu(self):
        # implementar diretorio e cota
        switcher = {1: self.diretorio, 2: self.__controlador_conta.ver_dados, 3: self.cota}
        self.menu_inical()
        while self.__usuario_ativo:
            opcao = self.__tela_sistema.tela_menu()
            if opcao == 0:
                self.__usuario_ativo = None
                self.menu_inical()
            else:
                switcher[opcao](self.usuario_ativo)


oi = Sistema()
oi.menu()
