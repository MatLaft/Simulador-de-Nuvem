import PySimpleGUI as sg
from view.tela_geral import Tela


class TelaSistema:
    def __init__(self):
        self.tela = Tela()
        self.__window = None

    def tela_login(self, opcao=None):
        if opcao == 1:
            pass
        else:
            retorno = ''
            return retorno

    def tela_menu_inicial(self):
        self.tela.botoestela(['Fechar', 'Login', 'Cadastrar'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao

    def tela_menu(self):
        self.tela.botoestela(['Deslogar', 'Diretorio', 'Ver dados de Usuario'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao

    def tela_menu_admin(self):
        self.tela.botoestela(['Deslogar', 'Diretorio', 'Ver dados de Usuario',
                              'Ver logs do sistema'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL ADMIN')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao

    def teste(self,lista):
        layout = [[sg.Text('Log do sistema', size=(30, 1),
                           font='Lucida', justification='left')],
                  [sg.Listbox(values=lista,
                              select_mode='single', key='fac',
                              size=(100, 8))],
                  [sg.Button('Voltar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Meus Arquivos').Layout(layout)
        event, value = self.__window.Read()
        if event == "Voltar":
            self.__window.close()

    def close(self):
        self.__window.Close()
