import PySimpleGUI as sg
from testetelas import ExemploView

class TelaSistema:
    def __init__(self):
        self.tela = ExemploView()

    def tela_login(self, opcao=None):
        if opcao == 1:
            print('Login feito!')
        else:
            retorno = input('Digite 0 para voltar ao menu ou ENTER para tentar novamente: ')
            return retorno

    def tela_menu_inicial(self):
        # print("\n==========SISTEMA DE ARQUIVOS==========")
        # print('1 - Logar\n2 - Cadastrar Usuário\n\n0 - Fechar')
        self.tela.botoestela(['Fechar', 'Login', 'Cadastrar'], 'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao
        # while type(opcao) == str:
        #     try:
        #         opcao = int(opcao)
        #         if 2 < opcao or opcao < 0:
        #             raise ValueError
        #         return opcao
        #     except ValueError:
        #         print('###Entrada Invalida!Digite um numero entre 0 e 2!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
        #         print('1 - Logar\n2 - Cadastrar Usuário\n\n0 - Fechar')
        #         opcao = input('Opção: ')

    def tela_menu(self):
        # print("\n==========MENU SISTEMA==========")
        # print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
        # opcao = input('Opção: ')
        self.tela.botoestela(['Deslogar', 'Diretorio', 'Ver dados de Usuario'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        return opcao
        # while type(opcao) == str:
        #     try:
        #         opcao = int(opcao)
        #         if 2 < opcao or opcao < 0:
        #             raise IndexError
        #         return opcao
        #     except ValueError:
        #         print(
        #             '###Entrada Invalida! Digite um numero!')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
        #         print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
        #         opcao = input('Opção: ')
        #     except IndexError:
        #         print(
        #             '###Entrada Invalida!Digite um numero entre 0 e 2!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
        #         print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
        #         opcao = input('Opção: ')

    def tela_menu_admin(self):
        # print("\n==========MENU SISTEMA==========")
        # print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver logs do sistema \n\n0 - Deslogar')
        # opcao = input('Opção: ')
        self.tela.botoestela(['Deslogar', 'Diretorio', 'Ver dados de Usuario','Ver logs do sistema'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('MENU INICIAL ADMIN')]]
                             )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        while type(opcao) == str:
            try:
                opcao = int(opcao)
                if 3 < opcao or opcao < 0:
                    raise IndexError
                return opcao
            except ValueError:
                print(
                    '###Entrada Invalida! Digite um numero!')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver logs do sistema \n\n0 - Deslogar')
                opcao = input('Opção: ')
            except IndexError:
                print(
                    '###Entrada Invalida!Digite um numero entre 0 e 3!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver logs do sistema \n4 - Servidores \n\n0 - Deslogar')
                opcao = input('Opção: ')