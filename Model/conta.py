from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha
        self.__diretorio = diretorio
        self.__empresa = empresa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def diretorio(self):
        return self.__diretorio

    @diretorio.setter
    def diretorio(self, diretorio):
        if isinstance(diretorio, str):
            self.__diretorio = diretorio

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        if isinstance(empresa, str):
            self.__empresa = empresa
