import PySimpleGUI as sg
from testetelas import ExemploView

class TelaConta:
    def __init__(self):
        self.tela = ExemploView()

    def tela_alterar_conta(self):
        # print('Deseja alterar algum dado?')
        # escolha = input('1 - para sim\n2 - para não\nOpção: ').lower()
            # print('\nSelecione o que deseja alterar!')
            # opcoes = '1 - nome   2 - email   3 - senha  0 - retornar'
            # print(opcoes)
            # op = input('Opção: ')
        self.tela.botoestela(['Retornar', 'Nome', 'Email', 'Senha'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text('Selecione o que deseja alterar!')]]
                             )
        op = str(self.tela.open()[0])
        self.tela.close()
        return op
            # while type(op) == str:
            #     try:
            #         if 0 <= int(op) <= 3:
            #             op = int(op)
            #             return op
            #         else:
            #             raise IndexError
            #     except ValueError:
            #         print('\nERRO!!Digite um número!!')
            #         print(opcoes)
            #         op = input('Opção: ')
            #     except IndexError:
            #         print(opcoes)
            #         print('\nERRO!!Número digitado deve estar entre 1 e 3!!')
            #         print(opcoes)
            #         op = input('Opção: ')

    def tela_alterar_senha(self):
        primeira = input('Digite uma nova senha: ')
        segunda = input('Digite a senha novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('As senhas não são iguais! Digite novamente')
                primeira = input('Digite uma nova senha: ')
                segunda = input('Digite a senha novamente: ')
        return primeira

    def tela_alterar_nome(self):
        primeira = input('Digite um novo nome: ')
        segunda = input('Digite o nome novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('Os nomes não são iguais! Digite novamente')
                primeira = input('Digite um novo nome: ')
                segunda = input('Digite o nome novamente: ')
        return primeira

    def tela_alterar_email(self):
        primeira = input('Digite um novo email: ')
        segunda = input('Digite o email novamente: ')
        while True:
            if primeira == segunda:
                break
            else:
                print('Os emails não são iguais! Digite novamente')
                primeira = input('Digite um novo email: ')
                segunda = input('Digite o email novamente: ')
        return primeira

    def tela_login(self, opt=None):
        if opt == 1:
            cpf = input('CPF: ')
            senha = input('Senha: ')
            try:
                cpf = int(cpf)
            except ValueError:
                print('Digite um CPF válido')
            return cpf, senha
        else:
            print('CPF e/ou Senha incorreto(s)!')

    def tela_cadastro(self, cpfs):
        senha_adm = 'ADEMIR'
        print("Realizar cadastro de um usuário!")
        opcao = input('Aperte <ENTER> para continuar!')
        if opcao != 'ContaAdemir':
            opcao = '2'
        if opcao == 'ContaAdemir':
            senha = input('Senha para ADM: ')
            opcao = '1'
            while senha != senha_adm:
                senha = input('Senha inválida!\nSenha para ADM: ')
                if senha == '0':
                    opcao = '2'
                    break
        nome = input('Nome: ')
        while nome == '':
            print('Entrada de nome obrigatória')
            nome = input('Nome: ')
        cpf = input('CPF: ')
        while type(cpf) == str:
            try:
                cpf = int(cpf)
                if cpf in cpfs:
                    raise ValueError
            except ValueError:
                print('CPF inválido ou já cadastrado! Digite novamente')
                cpf = input('CPF: ')
        empresa = input('Empresa: ')
        while empresa == '':
            print('Entrada de empresa obrigatória')
            empresa = input('Empresa: ')
        email = input('Email: ')
        while email == '':
            print('Entrada de email obrigatória')
            email = input('Email: ')
        senha1 = input('Senha: ')
        while senha1 == '':
            print('Entrada de senha obrigatória')
            senha1 = input('senha: ')
        senha2 = input('Digite a senha novamente: ')
        while senha1 != senha2:
            print('Senha digitada pela segunda vez foi diferente da primeira')
            print('Digite novamente!')
            senha1 = input('Senha: ')
            while senha1 == '':
                print('Entrada de senha obrigatória')
                senha1 = input('senha: ')
            senha2 = input('Digite a senha novamente: ')
        return nome, cpf, empresa, email, senha1, opcao

    def tela_ver_dados(self, nome, cpf, email, empresa):
        # print('\n==========DADOS USUÁRIO==========')
        # print(f'Nome: {nome}\nCPF: {cpf}\nEmail: {email}\nEmpresa: {empresa}')
        self.tela.botoestela(['NAO','SIM'],
                             'SISTEMA DE ARQUIVOS',
                             [[sg.Text(f'Nome: {nome}')],
                              [sg.Text(f'CPF: {cpf}')],
                              [sg.Text(f'Email: {email}')],
                              [sg.Text(f'Empresa: {empresa}')],
                              [sg.Text('DESEJA ALTERAR ALGUM DADO DA CONTA?')]
                              ]
                             )
        op = str(self.tela.open()[0])
        self.tela.close()
        return op
