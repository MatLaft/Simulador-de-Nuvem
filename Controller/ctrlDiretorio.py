from Entities.diretorio import Diretorio, Usuario, Path
import os
import shutil
from Entities.servidor import Servidor
from View.telaDiretorio import *


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
        if isinstance(servidor, Servidor) and isinstance(usuario, Usuario):
            nome_servidor = os.path.dirname(servidor.endereco)
            path_dir = Path(nome_servidor + "\\" + usuario.empresa + "\\" + str(usuario.cpf))
            path_dir.mkdir(parents=True, exist_ok=True)
            novo_diretorio = Diretorio(usuario, path_dir, servidor.cota)
            self.__diretorios[usuario.cpf] = novo_diretorio
            return novo_diretorio

    def excluir_diretorio(self, diretorio: Diretorio):
        if isinstance(diretorio, Diretorio) and diretorio in self.__diretorios:
            self.__diretorios.remove(diretorio.path)
            try:
                os.remove(diretorio.path)
            except Exception:
                shutil.rmtree(diretorio.path)

    def ver_cota(self, diretorio: Diretorio):
        return diretorio.cota

    def mostrar_arquivos(self, diretorio: Diretorio):
        lista_arquivos = []
        for arquivos in diretorio.arquivos:
            lista_arquivos.append([arquivos.nome, arquivos.data, arquivos.tamanho])
        return lista_arquivos
