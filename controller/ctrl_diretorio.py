from model.diretorio import Diretorio, Usuario, Path
import os
from model.servidor import Servidor
from view.tela_diretorio import *
from model.conta import Conta
from DAO.diretorio_dao import DiretorioDao


class CtrlDiretorio:
    def __init__(self):
        self.__tela_diretorio = TelaDiretorio()
        self.__diretorios = {}

    @property
    def diretorios(self):
        return self.__diretorios

    @property
    def tela_diretorio(self):
        return self.__tela_diretorio

    def adicionar_diretorio(self, servidor: Servidor, usuario: Usuario):
        if isinstance(servidor, Servidor) and isinstance(usuario, Conta):
            nome_servidor = os.path.dirname(servidor.endereco)
            path_dir = Path(nome_servidor + "\\" + usuario.empresa + "\\" + str(usuario.cpf))
            path_dir.mkdir(parents=True, exist_ok=True)
            novo_diretorio = Diretorio(usuario, path_dir, servidor.cota)
            self.__diretorios[usuario.cpf] = novo_diretorio
            return novo_diretorio

    def ver_cota(self, diretorio: Diretorio):
        return diretorio.cota

    def mostrar_arquivos(self, diretorio: Diretorio):
        lista_arquivos = []
        for arquivos in diretorio.arquivos:
            lista_arquivos.append([arquivos.nome, arquivos.data, arquivos.tamanho])
        return lista_arquivos

    def menu_diretorio(self, usuario: Usuario):
        while True:
            opcao_diretorio = self.tela_diretorio.tela_principal_diretorio()
            if opcao_diretorio == 1:
                diretorio = self.diretorios[usuario.cpf]
                arquivos = self.mostrar_arquivos(diretorio)
                self.tela_diretorio.tela_ver_arquivos(arquivos)
            elif opcao_diretorio == 2:
                permanencia = 1
                while permanencia == 1:
                    diretorio = self.diretorios[usuario.cpf]
                    path = (self.tela_diretorio.tela_enviar_arquivo())
                    if path != "0":
                        validacao, permanencia = diretorio.adicionar_arquivo(path, usuario)
                        self.tela_diretorio.tela_mensagem(validacao)
                    else:
                        permanencia = 0
            elif opcao_diretorio == 3:
                diretorio = self.diretorios[usuario.cpf]
                arquivos = self.mostrar_arquivos(diretorio)
                excluido = self.tela_diretorio.tela_excluir_arquivo(arquivos)
                diretorio.excluir_arquivo(excluido)
            elif opcao_diretorio == 4:
                diretorio = self.diretorios[usuario.cpf]
                cota = self.ver_cota(diretorio)
                self.tela_diretorio.tela_cota(cota)
            else:
                break
