from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


def novo():
    # zerar score
    t.score.setText('0')
    # limpar botões
    for i in botoes:
        i.setText("")


def msg(titulo, texto):
    m = QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setWindowTitle(titulo)
    m.setText(texto)
    if m.exec() == QMessageBox.Ok:
        exit()


def vencedor(a):
    msg('fim', str(a) + ' venceu')


def evento(button):
    print(button.text())

    if button.text() != '':
        return

    j = getJogada()
    if j == '0':
        button.setStyleSheet('color : blue')
    else:
        button.setStyleSheet('color : red')

    button.setText(j)

    # verifica vencedor
    if all(j == e for e in [botoes[0].text(), botoes[1].text(), botoes[2].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[3].text(), botoes[4].text(), botoes[5].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[6].text(), botoes[7].text(), botoes[8].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[0].text(), botoes[3].text(), botoes[6].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[1].text(), botoes[4].text(), botoes[7].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[2].text(), botoes[5].text(), botoes[8].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[0].text(), botoes[4].text(), botoes[8].text()]):
        vencedor(j)
    elif all(j == e for e in [botoes[2].text(), botoes[4].text(), botoes[6].text()]):
        vencedor(j)


def getJogada():
    global vez
    if vez == '0':
        vez = 'X'
    else:
        vez = '0'
    return vez


vez = 0

# inicializando a janela
Form, Window = uic.loadUiType("tela.ui")
app = QApplication([])
window = Window()
t = Form()
t.setupUi(window)  # carrega os componentes

botoes = [t.b1, t.b2, t.b3, t.b4, t.b5, t.b6, t.b7, t.b8, t.b9]

# define os eventos dos botões
for i in botoes:
    i.clicked.connect(partial(evento, i))

# inicializa o jogo
novo()

# apresenta a janela
window.show()
app.exec()
