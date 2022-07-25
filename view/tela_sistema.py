import PySimpleGUI as sg
from view.tela_geral import Tela


class TelaSistema:
    def __init__(self):
        self.__tela = Tela()
        self.__window = None

    @property
    def tela(self):
        return self.__tela

    def tela_login(self, opcao=None):
        if opcao == 1:
            pass
        else:
            retorno = ''
            return retorno

    def tela_menu_inicial(self):
        self.tela.botoes_tela(['Fechar', 'Login', 'Cadastrar'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('MENU INICIAL')]]
                              )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao

    def tela_menu(self):
        self.tela.botoes_tela(['Deslogar', 'Diretorio', 'Ver dados de Usuario'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('MENU INICIAL')]]
                              )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao

    def tela_menu_admin(self):
        self.tela.botoes_tela(['Deslogar', 'Diretorio', 'Ver dados de Usuario',
                              'Ver logs do sistema'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('MENU INICIAL ADMIN')]]
                              )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao
