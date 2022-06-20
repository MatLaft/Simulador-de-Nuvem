from Entities.servidor import Servidor
from pathlib import Path


class CtrlServidor:
    def __init__(self):
        self.__servidores = list()
        self.__nome_empresas = list()

    @property
    def servidores(self):
        return self.__servidores

    @property
    def nome_empresas(self):
        return self.__nome_empresas

    def adicionar_servidor(self, empresa: str):
        if isinstance(empresa, str) and empresa not in self.__nome_empresas:
            endereco_servidor = Path("C:\Trabalho1\Servidores\\" + empresa)
            endereco_servidor.mkdir(parents=True, exist_ok=True)
            novo_servidor = Servidor(empresa, endereco_servidor)
            self.__servidores.append(novo_servidor)
            self.__nome_empresas.append(empresa)
            novo_servidor.log.incluir_log('Servidor criado')
            return novo_servidor
        else:
            return self.__servidores[self.__nome_empresas.index(empresa)]
