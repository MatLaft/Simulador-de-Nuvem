from Entities.servidor import Servidor
from pathlib import Path


class CtrlServidor:
    def __init__(self):
        self.__servidores = list()
        self.__nome_empresas = list()

    @property
    def servidores(self):
        return self.__servidores

    def adicionar_servidor(self, empresa: str):
        if isinstance(empresa, str) and empresa not in self.__nome_empresas:
            endereco_servidor = Path("C:\Trabalho1\Servidores\\" + empresa)
            endereco_servidor.mkdir(parents=True, exist_ok=True)
            novo_servidor = Servidor(empresa, endereco_servidor)
            self.__servidores.append(novo_servidor)
            self.__nome_empresas.append(empresa)
            return novo_servidor
