import PySimpleGUI as sg

# layout =[
#     [sg.Text('Incluir novo cliente')],
#     [sg.Text('Nome', size=(15, 1)), sg.InputText('',key= 'Nome')],
#     [sg.Text('Senha', size=(15, 1)), sg.InputText('', key= 'Senha')],
#     [sg.Text('ambibaue'),sg.FileBrowse()],
#     [sg.Button('Coé Patrão'),sg.Cancel()]
# ]
#
# window = sg.Window('Cadastro de clientes').layout(layout)
#
# button,values = window.read()
#
# print(button,values)


class Tela:
    def __init__(self):
        self.__window = None
        self.__layout = None

    def botoestela(self, botoes: list[''], titulo, botoeprontos: list = []):
        listabotoesprontos = botoeprontos
        listabotoes = []
        for i in botoes:
            listabotoes.append(sg.Button(f'{i}'))
        listabotoesprontos.append(listabotoes)
        self.__window = sg.Window(f'{titulo}').layout(listabotoesprontos)
        self.__layout = botoes

    def botoestelapersonalizado(self, listabotoesprontos,listanome,titulo):
        self.__window = sg.Window(f'{titulo}').layout(listabotoesprontos)
        self.__layout = listanome

    def open(self):
        button, values = self.__window.Read()
        if button is not None:
            return self.__layout.index(button), values
        else:
            return ['', values]

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

# oi = Tela()
# oi.botoestela(['NAO','SIM'],'ALTERAR CONTA',[ [sg.Text('Nome', size=(15, 1)), sg.InputText('',key= 'Nome')]])
# x = oi.open()[1]
# print(x)
# column1 = [
#     [sg.Text(f'Scrollable{i}')] for i in range(10)
# ]
#
# column2 = [
#     [sg.Text(f'Static{i}')] for i in range(5)
# ]
#
# layout = [
#     [
#         sg.Column(column1, scrollable=True,  vertical_scroll_only=True),
#         sg.Column(column2)
#     ]
# ]
#
# window = sg.Window('Scrollable', layout)
# event, values = window.read()
# window.close()
# sg.main_sdk_help()
