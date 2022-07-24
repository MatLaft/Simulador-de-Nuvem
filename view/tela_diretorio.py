import PySimpleGUI as sg


class TelaDiretorio:
    def __init__(self):
        self.__window = None

    def tela_principal_diretorio(self):
        layout = [
            [sg.Button('Ver arquivos', button_color=('white', '#001480')),
             sg.Button('Adicionar arquivo', button_color=('white', '#007339')),
             sg.Button('Excluir arquivo', button_color=('white', '#007339')),
             sg.Button('Ver Cota de armazenamento',
                       button_color=('white', '#007339')),
             sg.Button('Voltar', button_color=('white', '#007339'))]]

        self.__window = sg.Window('MEU DIRETORIO').Layout(layout)

        event, values = self.__window.Read()
        if event == 'Ver arquivos':
            self.close()
            return 1
        if event == 'Adicionar arquivo':
            self.close()
            return 2
        if event == 'Excluir arquivo':
            self.close()
            return 3
        if event == 'Ver Cota de armazenamento':
            self.close()
            return 4
        if event == 'Voltar':
            self.close()
            return 0


    def tela_ver_arquivos(self, lista_arquivos: []):
        lista_concatenada = []
        for index, arquivo in enumerate(lista_arquivos):
            lista_concatenada.append(
                f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')
        layout = [[sg.Text('Escolha o arquivo a ser excluído', size=(30, 1),
                           font='Lucida', justification='left')],
                  [sg.Listbox(values=lista_concatenada,
                              select_mode='single', key='fac',
                              size=(100, 8))],
                   [sg.Button('Voltar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Meus Arquivos').Layout(layout)
        event, value = self.__window.Read()
        if event == "Voltar":
            self.close()

    def tela_enviar_arquivo(self):
        layout = [[sg.T("")],
                  [sg.Text("Escolha um Arquivo: "),
                   sg.InputText(key="path"), sg.FileBrowse()],
                  [sg.Button("Enviar")],
                  [sg.Button("Voltar")]]

        self.__window = sg.Window('Busca de Arquivo', layout, size=(600, 150))
        event, value = self.__window.Read()
        if event == "Enviar":
            arquivo_path = value["path"]
            self.close()
            return str(arquivo_path)
        if event == "Voltar":
            self.close()
            return str(0)

    def tela_excluir_arquivo(self, lista_arquivos: []):
        lista_concatenada = []
        for index, arquivo in enumerate(lista_arquivos):
            lista_concatenada.append(f'{index + 1} - {arquivo[0]} {arquivo[1]} {arquivo[2]} KB')
        layout = [[sg.Text('Escolha o arquivo a ser excluído', size=(30, 1),
                             font='Lucida', justification='left')],
                  [sg.Listbox(values=lista_concatenada,
                                select_mode='single', key='fac',
                                size=(100, 8), )],
                  [sg.Button('Excluir', font=('Times New Roman', 12)),
                   sg.Button('Voltar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Excluir Arquivo').Layout(layout)
        event, value = self.__window.Read()
        if event == "Excluir":
            self.close()
            return int(value['fac'][0][0]) - 1
        if event == "Voltar":
            self.close()
            return None


    def tela_cota(self, cota: int):
        self.mostra_mensagem(f"\nA cota restante é: {cota:.2f} KB")

    def tela_mensagem(self, mensagem: str):
        self.mostra_mensagem(mensagem)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
