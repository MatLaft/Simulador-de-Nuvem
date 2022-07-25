from controller.ctrl_conta import *
from controller.ctrl_diretorio import *
from controller.ctrl_servidor import *
from view.tela_sistema import *
from controller.ctrl_logs import Log


class Sistema:
    def __init__(self):
        self.__controlador_servidor = CtrlServidor()
        self.__controlador_conta = CtrlConta()
        self.__controlador_diretorio = CtrlDiretorio()
        self.__usuario_ativo = None
        self.__tela_sistema = TelaSistema()
        self.__log = Log()

    @property
    def usuario_ativo(self):
        return self.__usuario_ativo

    @property
    def log(self):
        return self.__log

    def logar(self):
        self.__usuario_ativo = self.__controlador_conta.logar()


    def menu_inical(self):
        while self.__usuario_ativo is None:
            opcao = self.__tela_sistema.tela_menu_inicial()
            if opcao == '0':
                return
            elif opcao == '1':
                self.logar()
            elif opcao == '2':
                novo_usuario = self.__controlador_conta.cadastrar_conta()
                if novo_usuario is None:
                    pass
                elif isinstance(novo_usuario, Usuario):
                    self.log.incluir_log(f'Usuario Cadastrado {novo_usuario.cpf}')
                    novo_servidor = self.__controlador_servidor.adicionar_servidor(
                        novo_usuario.empresa)
                    self.log.incluir_log(
                        f'Servidor {novo_usuario.empresa} criado ')
                    novo_diretorio = self.__controlador_diretorio.adicionar_diretorio(
                        novo_servidor, novo_usuario)
                    novo_servidor.diretorios.append(novo_diretorio)
                    self.log.incluir_log(
                        f'Diretório {novo_usuario.cpf} adicionado')
                elif isinstance(novo_usuario, Admin):
                    self.log.incluir_log(f'Administrador Cadastrado {novo_usuario.cpf}')
                    novo_servidor = self.__controlador_servidor.adicionar_servidor(novo_usuario.empresa)
                    self.log.incluir_log(f'Servidor {novo_usuario.empresa} criado ')
                    novo_diretorio = self.__controlador_diretorio.adicionar_diretorio(novo_servidor, novo_usuario)
                    novo_servidor.diretorios.append(novo_diretorio)
                    self.log.incluir_log(f'Diretório {novo_usuario.cpf} adicionado')
            elif opcao == '':
                return

    def menu(self):
        self.menu_inical()
        while isinstance(self.__usuario_ativo, Conta):
            if isinstance(self.__usuario_ativo, Usuario):
                opcao = (self.__tela_sistema.tela_menu())
                if opcao == '0':
                    self.usuario_ativo.log.incluir_log('Saiu do sistema', self.usuario_ativo)
                    self.__usuario_ativo = None
                    self.menu_inical()
                elif opcao == '1':
                    self.__controlador_diretorio.menu_diretorio(self.__usuario_ativo)
                elif opcao == '2':
                    self.__controlador_conta.ver_dados(self.__usuario_ativo)
            else:
                opcao = (self.__tela_sistema.tela_menu_admin())
                if opcao == '0':
                    self.usuario_ativo.log.incluir_log('Saiu do sistema',
                                                       self.usuario_ativo)
                    self.__usuario_ativo = None
                    self.menu_inical()
                elif opcao == '1':
                    self.__controlador_diretorio.menu_diretorio(
                        self.__usuario_ativo)
                elif opcao == '2':
                    self.__controlador_conta.ver_dados(self.__usuario_ativo)
                elif opcao == '3':
                    historico = list(self.log.log)
                    self.__tela_sistema.teste(historico)
