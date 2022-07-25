

class ExcluirArquivoException(Exception):
    def __init__(self) -> None:
        super().__init__("Você não selecionou um arquivo!")
