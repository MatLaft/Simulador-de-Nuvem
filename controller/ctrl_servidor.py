from model.servidor import Servidor
from pathlib import Path
from dao.servidor_dao import ServidorDao


class CtrlServidor:
    def __init__(self):
        self.__servidor_dao = ServidorDao()
        self.__nome_empresas = list()

    @property
    def servidores(self):
        return self.__servidor_dao.get_all()

    @property
    def nome_empresas(self):
        return self.__nome_empresas

    def adicionar_servidor(self, empresa: str):
        if isinstance(empresa, str) and empresa not in self.__nome_empresas:
            endereco_servidor = Path("C:\Trabalho1\Servidores\\" + empresa)
            endereco_servidor.mkdir(parents=True, exist_ok=True)
            novo_servidor = Servidor(empresa, endereco_servidor)
            self.__servidor_dao.add(novo_servidor)
            self.__nome_empresas.append(empresa)
            return novo_servidor
        else:
            return self.__servidor_dao.get([self.__nome_empresas.index(empresa)])
