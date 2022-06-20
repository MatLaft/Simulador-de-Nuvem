from Entities.usuario import *
from View.telaconta import *
from Entities.admin import *
from Controller.ctrlDiretorio import *
from Controller.ctrlServidor import *


class CtrlConta:
    def __init__(self):
        self.__contas = {123:Admin('Adm',1,'adm','adm','1','ADM'),}
        self.__tela = TelaConta()

    @property
    def tela(self):
        return self.__tela

    @property
    def contas(self):
        return list(self.__contas.values())


    def relacao_cpf_nome(self):
        dados_tela = []
        for conta in self.__contas.values():
            dados_tela.append({'nome': conta.nome, 'cpf': conta.cpf})
        return dados_tela

    def ver_contas(self):
        return self.__tela.tela_contas(self.relacao_cpf_nome())

    def cadastrar_conta(self):
        nome, cpf, empresa, email, senha,opcao = self.__tela.tela_cadastro(self.__contas.keys())
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__contas.keys():
            diretorio = str(cpf)
            if opcao == '2':
                usuario = Usuario(nome, cpf, email, senha, diretorio, empresa)
                self.__contas[usuario.cpf] = usuario
                return usuario
            elif opcao == '1':
                adm = Admin(nome, cpf, email, senha, diretorio, empresa)
                self.__contas[adm.cpf] = adm
                return adm

    def alterar_conta(self, conta):
        conta_selecionada = conta
        opcao = self.__tela.tela_alterar_conta()
        if opcao == 1:
            conta_selecionada.nome = self.__tela.alterar_nome()
            conta_selecionada.log.incluir_log('Nome alterado')
        elif opcao == 2:
            conta_selecionada.email = self.__tela.alterar_email()
            conta_selecionada.log.incluir_log('Email alterado')
        elif opcao == 3:
            conta_selecionada.senha = self.__tela.alterar_senha()
            conta_selecionada.log.incluir_log('Senha alterada')
        elif opcao == 0:
            return

    def logar(self):
        cpf, senha = self.__tela.tela_login(1)
        for i in self.__contas.values():
            if i.cpf == cpf and i.senha == senha:
                i.log.incluir_log('Entrou no sistema')
                return i
        else:
            self.__tela.tela_login()
            return

    def ver_dados(self, conta):
        nome, cpf, email, empresa= conta.nome, conta.cpf, conta.email, conta.empresa
        self.__tela.tela_ver_dados(nome, cpf, email, empresa)
        self.alterar_conta(conta)
