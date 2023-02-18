from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


def novo():
    # limpar botões
    for i in botoes:
        i.setText("")


def limpar():
    atualizar()
    novo()


def atualizar():
    t.scoreX.setText(str(pontosX))
    t.score0.setText(str(pontos0))


def msg(titulo, texto):
    m = QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setWindowTitle(titulo)
    m.setText(texto)
    if m.exec() == QMessageBox.Ok:
        limpar()


def vencedor(a):
    global pontos0, pontosX
    if a == '0':
        pontos0 += 1
    else:
        pontosX += 1
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
    if all(j == b.text() for b in [botoes[0], botoes[1], botoes[2]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[3], botoes[4], botoes[5]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[6], botoes[7], botoes[8]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[0], botoes[3], botoes[6]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[1], botoes[4], botoes[7]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[2], botoes[5], botoes[8]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[0], botoes[4], botoes[8]]):
        vencedor(j)
    elif all(j == b.text() for b in [botoes[2], botoes[4], botoes[6]]):
        vencedor(j)
    elif all(b.text() != '' for b in botoes):
        msg('fim', 'Empatou')


def getJogada():
    global vez
    if vez == '0':
        vez = 'X'
    else:
        vez = '0'
    return vez


vez = 0
pontos0 = 0
pontosX = 0

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
# zerar score
t.scoreX.setText('0')
t.score0.setText('0')
novo()

# apresenta a janela
window.show()
app.exec()
