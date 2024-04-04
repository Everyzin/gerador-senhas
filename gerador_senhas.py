import random
import PySimpleGUI as sg
import os


class SenhaGen:
    def __init__(self):
        # Layout
        sg.theme('DarkBlue4')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(key='senha_gerada', size=(32, 5))],
            [sg.Button('Gerar Senha', size=(11, 2)), sg.Button('Salvar', size=(7, 2)), sg.CloseButton('Sair', size=(7, 2))],
        ]
        # Declarar janela
        self.janela = sg.Window('Gerador de senhas', layout)

    def Iniciar(self):
        texto = ''
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                texto += (f"Site: {valores['site']} | usuario: {valores['usuario']} senha: {nova_senha}\n")
                print(f"Site: {valores['site']} | usuario: {valores['usuario']} senha: {nova_senha}")
            if evento == 'Salvar':
                self.salvar(texto)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        nova_senha = ''.join(chars)
        return nova_senha

    def salvar(self, texto):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"{texto}"
            )
        print('Arquivo salvo!')


gerador = SenhaGen()
gerador.Iniciar()
