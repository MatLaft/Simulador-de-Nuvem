from Model.usuario import *
from View.telausuario import *
from Model.admin import *


class CtrlConta:
    def __init__(self):
        self.__contas = {}
        self.__tela = TelaUsuario()

    def relacao_cpf_nome(self):
        dados_tela = []
        for conta in self.__contas.values():
            dados_tela.append({'nome': conta.nome, 'cpf': conta.cpf})
        return dados_tela

    def ver_contas(self):
        return self.__tela.tela_contas(self.relacao_cpf_nome())

    @property
    def contas(self):
        return list(self.__contas.values())

    def cadastrar_usuario(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__contas.keys():
            usuario = Usuario(nome, cpf, email, senha, diretorio, empresa)
            self.__contas[usuario.cpf] = usuario

    def cadastrar_admin(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__contas.keys():
            admin = Admin(nome, cpf, email, senha, diretorio, empresa)
            self.__contas[admin.cpf] = admin

    def remover_usuario(self, cpf):
        if cpf in self.__contas.keys():
            for i in self.__contas:
                if i.cpf == cpf:
                    del self.__contas[i]

    def selecionar_usuario(self):
        conta_selecionada = self.__tela.tela_escolher_conta(self.relacao_cpf_nome())
        while type(conta_selecionada) == str:
            try:
                return self.__contas[int(conta_selecionada)]
            except ValueError:
                print('Digite um CPF valido')
                conta_selecionada = self.__tela.tela_escolher_conta(self.relacao_cpf_nome())

            except KeyError:
                print(f'CPF nao cadastrado!')
                conta_selecionada = self.__tela.tela_escolher_conta(self.relacao_cpf_nome())

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
        for i in self.__contas.values():
            if i.cpf == cpf and senha:
                return i
            else:
                self.__tela.tela_login()
                return
