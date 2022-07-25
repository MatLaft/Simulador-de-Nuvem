import PySimpleGUI as sg
from view.tela_geral import Tela
from Erros.cpf_duplicado_exception import CPFDuplicadoException


class TelaConta:
    def __init__(self):
        self.tela = Tela()

    def tela_alterar_conta(self):
        self.tela.botoes_tela(['Retornar', 'Nome', 'Email', 'Senha'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('Selecione o que deseja alterar!')]]
                              )
        op = str(self.tela.open()[0])
        self.tela.close()
        return op

    def tela_alterar_senha(self):
        # primeira = input('Digite uma nova senha: ')
        # segunda = input('Digite a senha novamente: ')
        self.tela.botoes_tela(['Retornar', 'Alterar Senha'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('Nova senha: ', size=(15, 1)),
                               sg.InputText('', key='senha1',
                                            password_char='*')],
                              [sg.Text('Repetir nova senha', size=(15, 1)),
                               sg.InputText('', key='senha2',
                                            password_char='*')]]
                              )

        acesso = (self.tela.open())
        primeira = acesso[1]['senha1']
        segunda = acesso[1]['senha2']
        self.tela.close()
        if acesso[0] == 0:
            return
        while True:
            if primeira == segunda:
                break
            else:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Senhas incoerentes!')
                self.tela.botoes_tela(['Retornar', 'Alterar Senha'],
                                     'SISTEMA DE ARQUIVOS',
                                      [[sg.Text('Nova senha: ', size=(15, 1)),
                                       sg.InputText('', key='senha1',
                                                    password_char='*')],
                                      [sg.Text('Repetir nova senha',
                                               size=(15, 1)),
                                       sg.InputText('', key='senha2',
                                                    password_char='*')]]
                                      )

                acesso = (self.tela.open())
                primeira = acesso[1]['senha1']
                segunda = acesso[1]['senha2']
                self.tela.close()
                if acesso[0] == 0:
                    return
        return primeira

    def tela_alterar_nome(self):
        self.tela.botoes_tela(['Retornar', 'Alterar nome'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('Novo Nome: ', size=(15, 1)),
                               sg.InputText('', key='nome1',)],
                              [sg.Text('Repetir novo nome: ',
                                       size=(15, 1)),
                               sg.InputText('', key='nome2')]]
                              )

        acesso = (self.tela.open())
        primeira = acesso[1]['nome1']
        segunda = acesso[1]['nome2']
        self.tela.close()
        if acesso[0] == 0:
            return
        while True:
            if primeira == segunda:
                break
            else:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Nomes incoerentes!')
                self.tela.botoes_tela(['Retornar', 'Alterar nome'],
                                     'SISTEMA DE ARQUIVOS',
                                      [[sg.Text('Novo nome: ', size=(15, 1)),
                                       sg.InputText('', key='nome1')],
                                      [sg.Text('Repetir novo nome: ',
                                               size=(15, 1)),
                                       sg.InputText('', key='nome2')]]
                                      )

                acesso = (self.tela.open())
                primeira = acesso[1]['nome1']
                segunda = acesso[1]['nome2']
                self.tela.close()
                if acesso[0] == 0:
                    return
        return primeira

    def tela_alterar_email(self):
        self.tela.botoes_tela(['Retornar', 'Alterar email'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('Novo email: ', size=(15, 1)),
                               sg.InputText('', key='email1')],
                              [sg.Text('Repetir novo email: ',
                                       size=(15, 1)),
                               sg.InputText('', key='email2')]]
                              )

        acesso = (self.tela.open())
        primeira = acesso[1]['email1']
        segunda = acesso[1]['email2']
        self.tela.close()
        if acesso[0] == 0:
            return
        while True:
            if primeira == segunda:
                break
            else:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Emails incoerentes')
                self.tela.botoes_tela(['Retornar', 'Alterar email'],
                                     'SISTEMA DE ARQUIVOS',
                                      [[sg.Text('Novo email: ', size=(15, 1)),
                                       sg.InputText('', key='email1')],
                                      [sg.Text('Repetir novo email: ',
                                               size=(15, 1)),
                                       sg.InputText('', key='email2')]]
                                      )

                acesso = (self.tela.open())
                primeira = acesso[1]['email1']
                segunda = acesso[1]['email2']
                self.tela.close()
                if acesso[0] == 0:
                    return
        return primeira

    def tela_login(self, opt=None):
        if opt == 1:
            self.tela.botoes_tela(['Retornar', 'Logar'],
                                 'SISTEMA DE ARQUIVOS',
                                  [[sg.Text('CPF', size=(15, 1)),
                                   sg.InputText('', key='CPF')],
                                  [sg.Text('Senha', size=(15, 1)),
                                   sg.InputText('', key='Senha',
                                                password_char='*')]]
                                  )

            acesso = (self.tela.open())
            cpf = acesso[1]['CPF']
            senha = acesso[1]['Senha']
            self.tela.close()
            if acesso[0] == 0:
                return None, None
            while True:
                try:
                    cpf = int(cpf)
                    return cpf, senha
                except ValueError:
                    # print('Digite um CPF válido')
                    self.tela.show_message('ERRO DE ENTRADA!',
                                           'Digite um CPF válido')
                    self.tela.botoes_tela(['Retornar', 'Logar'],
                                         'SISTEMA DE ARQUIVOS',
                                          [[sg.Text('CPF', size=(15, 1)),
                                           sg.InputText('', key='CPF')],
                                          [sg.Text('Senha', size=(15, 1)),
                                           sg.InputText('', key='Senha',
                                                        password_char='*')]]
                                          )
                    acesso = (self.tela.open())
                    cpf = acesso[1]['CPF']
                    senha = acesso[1]['Senha']
                    self.tela.close()
                    if acesso[0] == 0:
                        return None, None
        else:
            self.tela.show_message('ERRO DE ENTRADA!',
                                   'CPF e/ou Senha incorreto(s)!')

    def tela_cadastro(self, cpfs):
        while True:
            self.tela.botoes_tela(['Retornar', 'Cadastrar!'],
                                 'ERRO DE ENTRADA!',
                                  [[sg.Text('Nome', size=(15, 1)),
                                   sg.InputText('', key='Nome')],
                                  [sg.Text('CPF', size=(15, 1)),
                                   sg.InputText('', key='CPF')],
                                  [sg.Text('Empresa', size=(15, 1)),
                                   sg.InputText('', key='Empresa')],
                                  [sg.Text('Email', size=(15, 1)),
                                   sg.InputText('', key='Email')],
                                  [sg.Text('Senha', size=(15, 1)),
                                   sg.InputText('', key='Senha1',
                                                password_char='*')],
                                  [sg.Text('Confirmar Senha', size=(15, 1)),
                                   sg.InputText('', key='Senha2',
                                                password_char='*')]]
                                  )
            acesso = (self.tela.open())
            nome = acesso[1]['Nome']
            cpf = acesso[1]['CPF']
            empresa = acesso[1]['Empresa']
            email = acesso[1]['Email']
            senha1 = acesso[1]['Senha1']
            senha2 = acesso[1]['Senha2']
            self.tela.close()
            if acesso[0] == 0:
                return None, None, None, None, None
            if nome == '':
                self.tela.show_message('ERRO DE ENTRADA!', 'Entrada de nome'
                                                              ' obrigatória')
            try:
                cpf = int(cpf)
                if cpf in cpfs:
                    raise CPFDuplicadoException
            except ValueError:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'CPF inválido!')
            except CPFDuplicadoException:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'CPF já cadastrado!')
                cpf = ''
            if empresa == '':
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Entrada de empresa obrigatória')
            if email == '':
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Entrada de email obrigatória')
            if senha1 == '':
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Entrada de senha obrigatória')
            if senha1 != senha2:
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Confirmação de senha incoerente.'
                                       ' Digite novamente!')
                senha1 = ''
            if not (nome == '' or cpf == '' or empresa == '' or email == ''
                    or senha1 == ''):
                return nome, cpf, empresa, email, senha1

    def tela_admin_usuario(self):
        self.tela.botoes_tela(['Retornar', 'Criar usuario',
                              'Criar Administrador'],
                             'SISTEMA DE ARQUIVOS',
                              [[sg.Text('Selecione a opcao o tipo de conta que'
                                       'deseja criar!')]]
                              )
        opcao = str(self.tela.open()[0])
        self.tela.close()
        if opcao == '2':
            while True:
                self.tela.botoes_tela(['Voltar', 'Desbloquear'],
                                     'SISTEMA DE ARQUIVOS',
                                      [[sg.Text('Código: ', size=(15, 1)),
                                      sg.InputText('', key='Codigo')]]
                                      )
                acesso = (self.tela.open())
                codigo = acesso[1]['Codigo']
                self.tela.close()
                if acesso[0] == 0:
                    return '0'
                elif codigo == 'ADEMIR':
                    return '2'
                self.tela.show_message('ERRO DE ENTRADA!',
                                       'Código Invalido!')
        return opcao

    def tela_ver_dados(self, nome, cpf, email, empresa):
        self.tela.botoes_tela(['NAO', 'SIM'],
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
