

class TelaConta:
    def __init__(self):
        pass

    def tela_contas(self, contas: list):
        print('Contas Cadastradas (Nome: CPF)')
        print('//', end='')
        for index, value in enumerate(contas):
            print(f'{value["nome"]}:{value["cpf"]}', end='//')
        print()

    def tela_escolher_conta(self, contas: list) -> str:
        self.tela_contas(contas)
        conta_selecionada = input("Selecione a conta que deseja pelo CPF: ")
        return conta_selecionada

    def tela_alterar_conta(self):
        print('Deseja alterar algum dado?')
        escolha = input('1 - para sim\n2 - para nao: ').lower()
        if escolha == '2':
            return
        elif escolha == '1':
            print('Selecione o que deseja alterar!')
            opcoes = '1 - nome   2 - email   3 - senha  0 - retornar'
            print(opcoes)
            op = input('Opcao: ')
            while type(op) == str:
                try:
                    if 0 <= int(op) <= 3:
                        op = int(op)
                        return op
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
        else:
            print('Escolha invalida')

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

    def tela_login(self, opt=None):
        if opt == 1:
            cpf = input('CPF: ')
            senha = input('Senha: ')
            try:
                cpf = int(cpf)
            except ValueError:
                print('Digite um CPF Válido')
            return cpf, senha
        else:
            print('CPF e/ou Senha incorreto(s)!')

    def tela_cadastro(self,cpfs):
        print("Realizar cadastro de um usuário!")
        opcao = input('1 - Administrador 2 - Usuário\n Opção: ')
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
                print('CPF invalido ou ja cadastrado! Digite novamente')
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
            print('Senha digitada pela segunda vez foi diferente da primera')
            print('Digite novamente!')
            senha1 = input('Senha: ')
            while senha1 == '':
                print('Entrada de senha obrigatória')
                senha1 = input('senha: ')
            senha2 = input('Digite a senha novamente: ')
        return nome, cpf, empresa, email, senha1, opcao

    def tela_ver_dados(self, nome, cpf, email, empresa):
        print(f'Nome: {nome}\nCPF: {cpf}\nEmail: {email}\nEmpresa: {empresa}')
