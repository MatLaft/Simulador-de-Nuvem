

class TelaDiretorio:
    def __init__(self):
        pass

    def tela_principal_diretorio(self):
        print("\n==========MEU DIRETÓRIO==========")
        print("1 - Ver arquivos")
        print("2 - Adicionar arquivo")
        print("3 - Excluir arquivo")
        print("4 - Ver Cota de armazenamento")
        print("\n0 - Voltar")
        opcao = input("Opção: ")
        while type(opcao) != int:
            try:
                opcao = int(opcao)
                if 0 <= opcao <= 4:
                    break
                else:
                    raise IndexError
            except ValueError:
                print("Digite um número!")
                opcao = input("Opção: ")
            except IndexError:
                print("Digite um número entre 0 e 4!")
                opcao = input("Opção: ")
        return opcao

    def tela_ver_arquivos(self, lista_arquivos: []):
        print("\n==========LISTA DE ARQUIVOS==========")
        if len(lista_arquivos) == 0:
            print("Não há arquivos no diretório!\n")
            return None
        else:
            for index, arquivo in enumerate(lista_arquivos):
                print(f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')

    def tela_enviar_arquivo(self):
        print("\n==========ENVIAR ARQUIVO==========")
        print("Digite o caminho do arquivo ex: C:\\\\diretorio\\\\arquivo.extensão \n\nDigite ""0"" para voltar")
        path = input("Caminho: ")
        return path

    def tela_excluir_arquivo(self, lista_arquivos: []):
        print("\n==========EXCLUIR ARQUIVO==========")
        print("Escolha o arquivo a ser excluído:")
        if len(lista_arquivos) == 0:
            print("Não há arquivos para excluir! \n")
            return None
        else:
            for index, arquivo in enumerate(lista_arquivos):
                print(f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')
            print("Digite ""0"" para voltar\n")
            arquivo = input("Arquivo: ")
            while type(arquivo) != int:
                try:
                    arquivo = int(arquivo)
                    if arquivo == 0:
                        return None
                    elif 1 <= arquivo <= len(lista_arquivos):
                        break
                    else:
                        raise IndexError
                except ValueError:
                    print("Digite um número!")
                    arquivo = input("Opção: ")
                except IndexError:
                    if len(lista_arquivos) == 1:
                        print("Digite o número 1")
                    else:
                        print("Digite um número entre 1 e " + str(len(lista_arquivos)))
                    arquivo = input("Opção: ")
            return arquivo - 1

    def tela_cota(self, cota: int):
        print(f"\nA cota restante é: {cota:.2f} KB")

    def tela_mensagem(self, mensagem: str):
        print(mensagem)
