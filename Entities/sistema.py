from Controller.ctrlconta import *
from Controller.ctrlDiretorio import *
from Controller.ctrlServidor import *
from View.telasistema import *


class Sistema:
    def __init__(self):
        self.__controlador_servidor = CtrlServidor()
        self.__controlador_conta = CtrlConta()
        self.__controlador_diretorio = CtrlDiretorio()
        self.__usuario_ativo = None
        self.__tela_sistema = TelaSistema()

    @property
    def usuario_ativo(self):
        return self.__usuario_ativo

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
                novo_usuario = self.__controlador_conta.cadastrar_usuario()
                novo_servidor = self.__controlador_servidor.adicionar_servidor(novo_usuario.empresa)
                novo_diretorio = self.__controlador_diretorio.adicionar_diretorio(novo_servidor, novo_usuario)
                novo_servidor.diretorios.append(novo_diretorio)
                print(novo_diretorio.path)

    def menu(self):
        # implementar diretorio e cota
        self.menu_inical()
        while self.__usuario_ativo:
            opcao = self.__tela_sistema.tela_menu()
            if opcao == 0:
                self.__usuario_ativo = None
                self.menu_inical()
            elif opcao == 1:
                while True:
                    opcao_diretorio = self.__controlador_diretorio.tela_diretorio.tela_principal_diretorio()
                    if opcao_diretorio == 1:
                        diretorio = self.__controlador_diretorio.diretorios[self.__usuario_ativo.cpf]
                        arquivos = self.__controlador_diretorio.mostrar_arquivos(diretorio)
                        self.__controlador_diretorio.tela_diretorio.tela_ver_arquivos(arquivos)
                    elif opcao_diretorio == 2:
                        path = (self.__controlador_diretorio.tela_diretorio.tela_enviar_arquivo())
                        diretorio = self.__controlador_diretorio.diretorios[self.__usuario_ativo.cpf]
                        validacao = diretorio.adicionar_arquivo(path, self.__usuario_ativo)
                        self.__controlador_diretorio.tela_diretorio.tela_mensagem(validacao)
                    elif opcao_diretorio == 3:
                        diretorio = self.__controlador_diretorio.diretorios[self.__usuario_ativo.cpf]
                        arquivos = self.__controlador_diretorio.mostrar_arquivos(diretorio)
                        excluido = self.__controlador_diretorio.tela_diretorio.tela_excluir_arquivo(arquivos)
                        diretorio.excluir_arquivo(excluido)
                    elif opcao_diretorio == 4:
                        diretorio = self.__controlador_diretorio.diretorios[self.__usuario_ativo.cpf]
                        cota = self.__controlador_diretorio.ver_cota(diretorio)
                        self.__controlador_diretorio.tela_diretorio.tela_cota(cota)
                    else:
                        break
            elif opcao == 2:
                self.__controlador_conta.ver_dados(self.__usuario_ativo)

if __name__ == "__main__":
    Sistema().menu()
#C:\\Users\\jv_dj\\Desktop\\teste.py
#C:\\Users\\jv_dj\\Desktop\\jv\\VIAGEM.png
#FileNotFoundError
