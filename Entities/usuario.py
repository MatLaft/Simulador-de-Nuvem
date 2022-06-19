from Entities.conta import Conta


class Usuario(Conta):
    def __init__(self, nome: str, cpf: int, email: str, senha: str, diretorio: str, empresa: str):
        super().__init__(nome, cpf, email, senha, diretorio, empresa)
        self.__admin = False
