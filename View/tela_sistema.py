

class TelaSistema:
    def __init__(self):
        pass

    def tela_login(self, opcao=None):
        if opcao == 1:
            print('Login feito!\n')
        else:
            retorno = input('Digite 0 para voltar ao menu ou ENTER para tentar novamente: ')
            return retorno

    def tela_menu_inicial(self):
        print("\n==========SISTEMA DE ARQUIVOS==========")
        print('1 - Logar\n2 - Cadastrar Usuário\n0 - Fechar')
        opcao = input('Opção: ')
        while type(opcao) == str:
            try:
                opcao = int(opcao)
                if 2 < opcao or opcao < 0:
                    raise ValueError
                return opcao
            except ValueError:
                print('###Entrada Invalida!Digite um numero entre 0 e 2!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Logar\n2 - Cadastrar Usuário\n0 - Fechar')
                opcao = input('Opção: ')

    def tela_menu(self):
        print("\n==========MENU SISTEMA==========")
        print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
        opcao = input('Opção: ')
        while type(opcao) == str:
            try:
                opcao = int(opcao)
                if 2 < opcao or opcao < 0:
                    raise IndexError
                return opcao
            except ValueError:
                print(
                    '###Entrada Invalida! Digite um numero!')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
                opcao = input('Opção: ')
            except IndexError:
                print(
                    '###Entrada Invalida!Digite um numero entre 0 e 2!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Diretorio \n2 - Ver dados de Usuario\n \n0 - Deslogar')
                opcao = input('Opção: ')

    def tela_menu_admin(self):
        print("\n==========MENU SISTEMA==========")
        print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver logs do sistema \n\n0 - Deslogar')
        opcao = input('Opção: ')
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
                print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver logs do sistema \n4 - Servidores \n0 - Deslogar')
                opcao = input('Opção: ')