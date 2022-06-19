from Entities.arquivo import Arquivo
from pathlib import Path
import shutil
import os
from datetime import datetime
from Entities.usuario import Usuario


class Diretorio:
    def __init__(self, usuario: Usuario, path: Path, cota: int):
        self.__usuario = usuario
        self.__cota = cota
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

    @property
    def arquivos(self):
        return self.__arquivos

    @path.setter
    def path(self, path: Path):
        self.__path = path

    def adicionar_arquivo(self, path: str, usuario: Usuario):
        try:
            if isinstance(path, str):
                path_origem = Path(path)
                nome_arquivo = os.path.basename(path_origem)
                tamanho = os.path.getsize(path_origem)
                if tamanho < 1024:
                    tamanho = (tamanho/1024)
                else:
                    tamanho = int(tamanho//1024)
                nome_diretorio = os.path.dirname(self.__path)
                arquivo = open(nome_diretorio + '\\' + str(usuario.cpf) + '\\' + nome_arquivo, "a")
                path_colar = Path(nome_diretorio + '\\' + str(usuario.cpf) + '\\' + nome_arquivo)
                arquivo.close()
                shutil.copyfile(path_origem, path_colar)
                data = datetime.today().strftime('%Y-%m-%d %H:%M')
                novo_arquivo = Arquivo(nome_arquivo, tamanho, data, path_colar)
                self.__cota -= tamanho
                if self.__cota < 0:
                    self.__cota += tamanho
                    return 'Arquivo muito grande, verifique sua cota!\n'
                else:
                    self.__arquivos.append(novo_arquivo)
                    return 'Arquivo adicionado ao diretório!\n'
        except FileNotFoundError:
            return 'Verifique o caminho do arquivo, arquivo não encontrado!\n'

    def excluir_arquivo(self, arquivo: int):
        if isinstance(arquivo, int):
            excluido = self.__arquivos.pop(arquivo)
            os.remove(excluido.path)
