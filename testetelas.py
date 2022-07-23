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


class ExemploView:
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

    def botoestelapersonalizado(self,listabotoesprontos,listanome,titulo):
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

    def show_message(self,titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

# oi = ExemploView()
# oi.botoestela(['NAO','SIM'],'ALTERAR CONTA',[[sg.Text('Incluir novo cliente')]])
# x = oi.open()[0]
# print(x)