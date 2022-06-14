
class TelaSistema:
    def __init__(self):
        self.oi = None

    def tela_login(self, opcao=None):
        ola = self.oi
        if opcao == 1:
            print('Login feito!')
        else:
            retorno = input('Digite 0 para voltar ao menu ou ENTER para tentar novamente: ')
            return retorno

    def tela_menu_inicial(self):
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
        print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver cota\n \n0 - Deslogar')
        opcao = input('Opção: ')
        while type(opcao) == str:
            try:
                opcao = int(opcao)
                if 3 < opcao or opcao < 0:
                    raise ValueError
                return opcao
            except ValueError:
                print(
                    '###Entrada Invalida!Digite um numero entre 0 e 3!###')  # ALTERAR NO FUTURO CONFORME ADICIONAR OPCAO
                print('1 - Diretorio \n2 - Ver dados de Usuario\n3 - Ver cota\n \n0 - Deslogar')
                opcao = input('Opção: ')
