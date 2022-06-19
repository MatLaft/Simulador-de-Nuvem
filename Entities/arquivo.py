from pathlib import Path


class Arquivo:
    def __init__(self, nome: str, tamanho: int, data: str, path: Path):
        self.__nome = nome
        self.__tamanho = tamanho
        self.__data = data
        self.__path = path

    @property
    def nome(self):
        return self.__nome

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def data(self):
        return self.__path

    @property
    def path(self):
        return self.__path

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
