

class CPFDuplicadoException(Exception):
    def __init__(self) -> None:
        super().__init__("CPF já cadastrado")
