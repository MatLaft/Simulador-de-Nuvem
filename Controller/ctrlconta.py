from Model.usuario import *
from View.telausuario import *
from Model.admin import *


class CtrlUsuario:
    def __init__(self):
        self.__contas = {}
        self.__tela = TelaUsuario()

    def ver_contas(self):
        return self.__tela.tela_contas(list(self.__contas.keys()))

    @property
    def contas(self):
        return list(self.__contas.keys())

    def cadastrar_usuario(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__contas.values():
            usuario = Usuario(nome, cpf, email, senha, diretorio, empresa)
            self.__contas[usuario] = usuario.cpf

    def cadastrar_admin(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__contas.values():
            admin = Admin(nome, cpf, email, senha, diretorio, empresa)
            self.__contas[admin] = admin.cpf

    def remover_usuario(self, cpf):
        if cpf in self.__contas.values():
            for i in self.__contas:
                if i.cpf == cpf:
                    del self.__contas[i]

    def selecionar_usuario(self):
        conta_selecionada = self.__tela.tela_escolher_conta(list(self.__contas.keys()))
        while type(conta_selecionada) == str:
            try:
                if int(conta_selecionada) >= 1:
                    conta_selecionada = int(conta_selecionada) - 1
                    return list(self.__contas.keys())[conta_selecionada]
                else:
                    raise IndexError

            except ValueError:
                print('Digite um Numero!')
                conta_selecionada = self.__tela.tela_escolher_conta(list(self.__contas.keys()))

            except IndexError:
                print(f'O Número digitado deve estar entre 1 e {len(list(self.__contas.keys()))}')
                conta_selecionada = self.__tela.tela_escolher_conta(list(self.__contas.keys()))

    def alterar_conta(self):
        conta_selecionada = self.selecionar_usuario()
        opcao = self.__tela.tela_alterar_conta()
        if opcao == 1:
            conta_selecionada.nome = self.__tela.alterar_nome()
        elif opcao == 2:
            conta_selecionada.email = self.__tela.alterar_email()
        elif opcao == 3:
            conta_selecionada.senha = self.__tela.alterar_senha()
        elif opcao == 0:
            return

    def logar(self):
        cpf, senha = self.__tela.tela_login(1)
        for i in self.__contas.keys():
            if i.cpf == cpf and senha:
                return i
            else:
                self.__tela.tela_login()
                return
