from Controller.ctrlDiretorio import *
from Controller.ctrlServidor import *
from Controller.ctrlconta import *
from View.telasistema import *


class CtrlSistema:
    def __init__(self):
        self.__ctrl_servidor = CtrlServidor()
        self.__ctrl_diretorio = CtrlDiretorio()
        self.__ctrl_conta = CtrlConta()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        while True:
            opcao_escolhida = self.__tela_sistema.tela_menu_inicial()
            if opcao_escolhida == 1:
                if self.__ctrl_conta.logar():
                    self.__tela_sistema.tela_menu()
            elif opcao_escolhida == 2:
                self.__ctrl_conta.cadastrar_usuario()
            elif opcao_escolhida == 0:
                break
