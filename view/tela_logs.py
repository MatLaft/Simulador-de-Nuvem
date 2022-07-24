import PySimpleGUI as sg
from view.tela_geral import Tela


class TelaLog:
    def __init__(self):
        self.tela = Tela()

    def print_logs(self, lista_historico: list):
        # print('\n==========LOGS DO SISTEMA==========')
        # for log in lista_historico:
        #     print(log)
        column1 = [
                [sg.Text(f'{i}')] for i in lista_historico]
        self.tela.botoestelapersonalizado(
            [[sg.Column(column1, scrollable=True,
                        vertical_scroll_only=True,
                        size=[500,500])], [sg.Button('Voltar')]],
            ['Voltar'],
            'SISTEMA DE ARQUIVOS')
        str(self.tela.open())
        self.tela.close()
