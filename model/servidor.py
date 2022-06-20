from pathlib import Path
from model.logs import Log


class Servidor:
    def __init__(self, nome_empresa: str, endereco: Path):
        self.__nome_empresa = nome_empresa
        self.__endereco = Path(endereco)
        self.__diretorios = []
        self.__cota = 10000

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    @property
    def endereco(self):
        return self.__endereco

    @property
    def diretorios(self):
        return list(self.__diretorios)

    @property
    def cota(self):
        return self.__cota
