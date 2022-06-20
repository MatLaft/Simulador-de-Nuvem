from Controller.ctrlconta import *
from Controller.ctrlDiretorio import *
from Controller.ctrlServidor import *
from View.telasistema import *
from Entities.logs import Log


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
        while True:
            self.__usuario_ativo = self.__controlador_conta.logar()
            if self.usuario_ativo:
                self.__tela_sistema.tela_login(1)
                break
            voltar = self.__tela_sistema.tela_login()
            if voltar == '0':
                break

    def menu_inical(self):
        while self.__usuario_ativo is None:
            opcao = self.__tela_sistema.tela_menu_inicial()
            if opcao == 0:
                return
            elif opcao == 1:
                self.logar()
            elif opcao == 2:
                novo_usuario = self.__controlador_conta.cadastrar_conta()
                if isinstance(novo_usuario, Usuario):
                    self.log.incluir_log(f'Usuario Cadastrado')
                elif isinstance(novo_usuario,Admin):
                    self.log.incluir_log(f'Administrador Cadastrado')
                novo_servidor = self.__controlador_servidor.adicionar_servidor(novo_usuario.empresa)
                self.log.incluir_log('Servidor criado')             ##CORRIGIR IMPLEMENTACAO_DE_CRIACAO_DUPLICADA
                novo_diretorio = self.__controlador_diretorio.adicionar_diretorio(novo_servidor, novo_usuario)
                novo_servidor.diretorios.append(novo_diretorio)
                self.log.incluir_log(f'Diretório {novo_usuario.cpf} adicionado')

    def menu(self):
        self.menu_inical()
        while self.__usuario_ativo:
            if isinstance(self.__usuario_ativo, Usuario):
                opcao = self.__tela_sistema.tela_menu()
                if opcao == 0:
                    self.usuario_ativo.log.incluir_log('Saiu do sistema')
                    for i in self.usuario_ativo.log.log:
                        self.log.incluir_log(f'{i}', self.__usuario_ativo, 'Sistema')
                    self.__usuario_ativo = None
                    self.menu_inical()
                elif opcao == 1:
                    self.__controlador_diretorio.menu_diretorio(self.__usuario_ativo)
                elif opcao == 2:
                    self.__controlador_conta.ver_dados(self.__usuario_ativo)
            else:
                opcao = self.__tela_sistema.tela_menu_admin()
                if opcao == 0:
                    self.usuario_ativo.log.incluir_log('Saiu do sistema')
                    for i in self.usuario_ativo.log.log:
                        if i not in self.log.log:
                            self.log.incluir_log(f'{i}',self.usuario_ativo,'Sistema')
                    self.__usuario_ativo = None
                    self.menu_inical()
                elif opcao == 1:
                    self.__controlador_diretorio.menu_diretorio(self.__usuario_ativo)
                elif opcao == 2:
                    self.__controlador_conta.ver_dados(self.__usuario_ativo)
                elif opcao == 3:
                    logs = self.log.log
                    self.log.tela_log.print_logs(logs)


# if __name__ == "__main__":
# Sistema().menu()
# C:\\Users\\jv_dj\\Desktop\\teste.py
# C:\\Users\\jv_dj\\Desktop\\jv\\VIAGEM.png
# C:\\Users\\jv_dj\\Downloads\\thonny-3.3.13.exe

oi = Sistema()
oi.menu()
# for i in oi.log.log:
#     print(i)
# print(oi._Sistema__controlador_servidor.nome_empresas)
# # for i in oi._Sistema__controlador_conta.contas:
# #     print(i.log.log)
# C:\\Users\\mathe\\Desktop\\Telas_Matheus_Eduardo.pdf
