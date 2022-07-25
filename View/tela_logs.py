import PySimpleGUI as sg
from view.tela_geral import Tela


class TelaLog:
    def __init__(self):
        self.tela = Tela()

    def print_logs(self, lista_historico: list):
        column1 = [
                [sg.Text(f'{i}')] for i in lista_historico]
        self.tela.botoes_tela_personalizado(
            [[sg.Column(column1, scrollable=True,
                        vertical_scroll_only=True,
                        size=[1000,500])], [sg.Button('Voltar')]],
            ['Voltar'],
            'SISTEMA DE ARQUIVOS')
        str(self.tela.open())
        self.tela.close()
