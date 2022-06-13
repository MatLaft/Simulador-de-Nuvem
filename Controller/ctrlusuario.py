from Model.usuario import *


class Ctrl_usuario:
    def __init__(self):
        self.__usuarios = {}
        self.__tela = None

    def cadastrar_usuario(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        if isinstance(nome, str) and isinstance(cpf, int) and isinstance(email, str) and isinstance(senha, str) \
                and isinstance(empresa, str) and cpf not in self.__usuarios.values():
            usuario = Usuario(nome, cpf, email, senha, diretorio, empresa)
            self.__usuarios[usuario] = usuario.cpf

    def remover_usuario(self, cpf):
        if cpf in self.__usuarios.values():
            for i in self.__usuarios:
                if i.cpf == cpf:
                    del self.__usuarios[i]


    def alterar_usuario(self):
