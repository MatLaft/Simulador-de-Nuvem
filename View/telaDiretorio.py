

class TelaDiretorio:
    def __init__(self):
        pass

    def tela_principal_diretorio(self):
        print("==========MEU DIRETÓRIO==========")
        print("1 - Ver arquivos")
        print("2 - Adicionar arquivo")
        print("3 - Excluir arquivo")
        print("4 - Ver Cota de armazenamento")
        print("0 - Voltar")
        opcao = int(input("Opcao: "))
        return opcao

    def tela_ver_arquivos(self):
        return

    def tela_enviar_arquivo(self):
        print("==========ENVIAR ARQUIVO==========")
        print("Digite o caminho do arquivo ex: (C:\\diretorio\\arquivo")
        path = input("Caminho:")
        return path

    def tela_excluir_arquivo(self):
        print("==========EXCLUIR ARQUIVO==========")
        print("Escolha o arquivo a ser excluído:")
        arquivo = int(input("Arquivo:"))
        return arquivo

    def tela_cota(self, cota: int):
        print("A cota restante é: " + str(cota) + "\n")
