

class TelaUsuario:
    def __init__(self):
        pass

    def tela_contas(self, contas: list):
        for index, value in enumerate(contas):
            print('Contas Cadastradas')
            print(f'{index+1} - {value.nome}:{value.cpf}', end=' ')
            print()

    def tela_escolher_conta(self, contas: list) -> str:
        self.tela_contas(contas)
        conta_selecionada = input("Selecione a conta que deseja: ")
        return conta_selecionada

    def tela_alterar_conta(self):
        print('Selecione o que deseja alterar:')
        opcoes = ('1 - nome   2 - email   3 - senha  0 - retornar')
        print(opcoes)
        op = input('Opcao: ')
        while type(op) == str:
            try:
                if 0 <= int(op) <= 3:
                    op = int(op)
                else:
                    raise IndexError
            except ValueError:
                print('ERRO!!Digite um numero!!')
                print(opcoes)
                op = input('Opcao: ')
            except IndexError:
                print(opcoes)
                print('ERRO!!Numero digitado deve estar entre 1 a 3!!')
                print(opcoes)
                op = input('Opcao: ')

    def alterar_senha(self):
        primeira = input('Digite uma nova senha: ')
        segunda = input('Digite a senha novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('A senhas nao sao iguais! Digite novamente')
                primeira = input('Digite uma nova senha: ')
                segunda = input('Digite a senha novamente: ')
        return primeira

    def alterar_nome(self):
        primeira = input('Digite um novo nome: ')
        segunda = input('Digite o nome novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('Os nomes nao sao iguais! Digite novamente')
                primeira = input('Digite um novo nome: ')
                segunda = input('Digite o nome novamente: ')
        return primeira

    def alterar_email(self):
        primeira = input('Digite um novo email: ')
        segunda = input('Digite o email novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('Os emails nao sao iguais! Digite novamente')
                primeira = input('Digite um novo email: ')
                segunda = input('Digite o email novamente: ')
        return primeira

    def tela_login(self,opt = None):
        if opt == 1:
            cpf = input('CPF: ')
            senha = input('Senha: ')
            return cpf, senha
        else:
            print('CPF e/ou Senha incorreto(s)!')
