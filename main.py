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
    # t.scoreX.setText(str(pontosX))
    t.scoreX.display(pontosX)
    t.score0.display(pontos0)


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


def question(titulo, texto):
    m = QMessageBox()
    m.setIcon(QMessageBox.Question)
    m.setWindowTitle(titulo)
    m.setText(texto)
    m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return m.exec()


def reset():
    if question('confirma?', 'Resetar jogo?') == QMessageBox.Ok:
        try:
            import os
            os.remove("score.dat")
            global pontos0, pontosX
            pontos0 = pontosX = 0
            atualizar()
        except:
            pass


def salvar():
    global pontos0, pontosX
    f = open('score.dat', 'w')
    dados = '0=' + str(pontos0) + ',x=' + str(pontosX)
    f.write(dados)
    f.close()


def carregar():
    global pontos0, pontosX
    try:
        f = open('score.dat', 'r')
        pontos = f.read().split(',')
        pontos0 = int(pontos[0].split('=')[1])
        pontosX = int(pontos[1].split('=')[1])
    except:
        print('arquivo não encontrado')
    atualizar()


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
app.aboutToQuit.connect(salvar)
window = Window()
t = Form()
t.setupUi(window)  # carrega os componentes

botoes = [t.b1, t.b2, t.b3, t.b4, t.b5, t.b6, t.b7, t.b8, t.b9]

# configuração inicial
t.score0.setStyleSheet('color : blue')
t.scoreX.setStyleSheet('color : red')

# define os eventos dos botões
t.reset.clicked.connect(reset)
for i in botoes:
    i.clicked.connect(partial(evento, i))

# atualizar score
atualizar()

# buscar score salvo
carregar()

# inicializa o jogo
novo()

# apresenta a janela
window.show()
app.exec()
