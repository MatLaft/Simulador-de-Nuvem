from Entities.arquivo import Arquivo
from pathlib import Path
import shutil
import os
from datetime import datetime
from Entities.usuario import Usuario


class Diretorio:
    def __init__(self, usuario: Usuario, path: Path):
        self.__usuario = usuario
        self.__cota = 0
        self.__arquivos = list()
        self.__path = path

    @property
    def usuario(self):
        return self.__usuario

    @property
    def cota(self):
        return self.__cota

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: Path):
        self.__path = path

    def adicionar_arquivo(self, path: str, usuario: Usuario):
        if isinstance(path, str):
            path_origem = Path(path)
            nome_arquivo = os.path.basename(path_origem)
            tamanho = os.path.getsize(path_origem)
            nome_diretorio = os.path.dirname(self.__path)
            arquivo = open(nome_diretorio + '\\' + str(usuario.cpf) + '\\' + nome_arquivo, "a")
            path_colar = Path(nome_diretorio + '\\' + str(usuario.cpf) + '\\' + nome_arquivo)
            arquivo.close()
            shutil.copyfile(path_origem, path_colar)
            data = datetime.today().strftime('%Y-%m-%d %H:%M')
            path_arquivo = Path(nome_diretorio + "\\" + nome_arquivo)
            novo_arquivo = Arquivo(nome_arquivo, tamanho, data, path_arquivo)
            self.__arquivos.append(novo_arquivo)

    def excluir_arquivo(self, arquivo: Arquivo):
        if isinstance(arquivo, Arquivo) and arquivo in self.__arquivos:
            self.__arquivos.remove(arquivo.path)
            os.remove(arquivo.path)


# path = Path('C:\\Trabalho1\\Servidores\\a\\1')
# user = Usuario("jv", 1, "ola", "1", "dir", "a")
# x = Diretorio(user, path)
# x.adicionar_arquivo('C:\\Users\\jv_dj\\Desktop\\teste.txt', user)
