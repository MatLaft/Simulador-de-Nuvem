from Entities.servidor import Servidor
from pathlib import Path
import os
import shutil


class CtrlServidor:
    def __init__(self):
        self.__servidores = list()

    @property
    def servidores(self):
        return self.__servidores

    def adicionar_servidor(self, empresa: str):
        if isinstance(empresa, str):
            endereco_servidor = Path("C:\Trabalho1\Servidores\\" + empresa)
            endereco_servidor.mkdir(parents=True, exist_ok=True)
            novo_servidor = Servidor(empresa, endereco_servidor)
            self.__servidores.append(novo_servidor)
            return novo_servidor

    def excluir_servidor(self, servidor: Servidor):
        if isinstance(servidor, Servidor) and servidor in self.__servidores:
            self.__servidores.remove(servidor)
            try:
                os.remove(servidor.endereco)
            except:
                shutil.rmtree(servidor.endereco)
