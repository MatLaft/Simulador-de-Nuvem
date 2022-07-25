from view.tela_conta import *
from model.admin import *
from controller.ctrl_diretorio import *
from dao.contaDAO import ContaDAO
from controller.ctrl_logs import CtrlLog


class CtrlConta:
    def __init__(self):
        self.__contas = ContaDAO()
        self.__tela_conta = TelaConta()

    @property
    def contas(self):
        return self.__contas.cache

    def relacao_cpf_nome(self):
        dados_tela = []
        for conta in self.contas.values():
            dados_tela.append({'nome': conta.nome, 'cpf': conta.cpf})
        return dados_tela

    def cadastrar_conta(self):
        opcao = self.__tela_conta.tela_admin_usuario()
        if opcao == '0' or opcao == '':
            return None
        nome, cpf, empresa, email, senha = \
            self.__tela_conta.tela_cadastro(self.contas.keys())
        if (nome is None and cpf is None
                and empresa is None and email is None and senha is None):
            return None
        if isinstance(nome, str) and isinstance(cpf, int) and\
                isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and \
                cpf not in self.contas.keys():
            diretorio = str(cpf)
            if opcao == '1':
                usuario = Usuario(nome, cpf, email, senha, diretorio, empresa)
                self.contas[usuario.cpf] = usuario
                self.__contas.add(usuario)
                return usuario
            elif opcao == '2':
                adm = Admin(nome, cpf, email, senha, diretorio, empresa)
                self.contas[adm.cpf] = adm
                self.__contas.add(adm)
                return adm

    def alterar_conta(self, conta):
        conta_selecionada = conta
        opcao = int(self.__tela_conta.tela_alterar_conta())
        if opcao == 1:
            novo_nome = self.__tela_conta.tela_alterar_nome()
            if novo_nome is None or novo_nome == '0':
                return
            conta_selecionada.nome = novo_nome
            CtrlLog().incluir_log('Nome alterado', conta)
            self.__contas.update()
        elif opcao == 2:
            novo_email = self.__tela_conta.tela_alterar_email()
            if novo_email is None or novo_email == '0':
                return
            conta_selecionada.email = novo_email
            CtrlLog().incluir_log('Email alterado', conta)
            self.__contas.update()
        elif opcao == 3:
            novo_senha = self.__tela_conta.tela_alterar_senha()
            if novo_senha is None or novo_senha == '0':
                return
            conta_selecionada.senha = novo_senha
            CtrlLog().incluir_log('Senha alterada', conta)
            self.__contas.update()
        elif opcao == 0:
            return

    def logar(self):
        while True:
            cpf, senha = self.__tela_conta.tela_login(1)
            if cpf is None and senha is None:
                return None
            for i in self.contas.values():
                if i.cpf == cpf and i.senha == senha:
                    CtrlLog().incluir_log('Entrou no sistema', i)
                    return i
            else:
                self.__tela_conta.tela_login()

    def ver_dados(self, conta):
        nome, cpf, email, empresa = conta.nome, conta.cpf, conta.email, \
                                    conta.empresa
        x = self.__tela_conta.tela_ver_dados(nome, cpf, email, empresa)
        if x == '1':
            self.alterar_conta(conta)
