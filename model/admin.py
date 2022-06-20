from model.conta import Conta


class Admin(Conta):
    def __init__(self, nome: str, cpf: int, email: str, senha: str, diretorio, empresa: str):
        super().__init__(nome, cpf, email, senha, diretorio, empresa)
        self.__admin = True
