

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

    def tela_ver_arquivos(self, lista_arquivos: []):
        print("==========LISTA DE ARQUIVOS==========")
        for index, arquivo in enumerate(lista_arquivos):
            print(f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')

    def tela_enviar_arquivo(self):
        print("==========ENVIAR ARQUIVO==========")
        print("Digite o caminho do arquivo ex: (C:\\\\diretorio\\\\arquivo")
        path = input("Caminho:")
        return path

    def tela_excluir_arquivo(self, lista_arquivos: []):
        print("==========EXCLUIR ARQUIVO==========")
        print("Escolha o arquivo a ser excluído:")
        for index, arquivo in enumerate(lista_arquivos):
            print(f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')
        arquivo = int(input("Arquivo:"))
        return arquivo - 1

    def tela_cota(self, cota: int):
        print("A cota restante é: " + str(cota) + "\n")

    def tela_mensagem(self, mensagem: str):
        print(mensagem)
