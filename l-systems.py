import turtle
from canvasvg import *

def LerArquivoTxt():
    f = open('Regras.txt', 'r')
    txt = f.read()
    return txt

txt = LerArquivoTxt()
txt = txt.split('\n')
variaveis = txt[0]
constantes = txt[1]
axioma = txt[2]
angulo = float(txt[3])
anguloInicial = float(txt[4])
numeroDeExecucoes = int(txt[5])
regrasTxt = list()
regras = list()

for i in range (6, len(txt)):
    regrasTxt.append(txt[i])
for i in regrasTxt:
    regra = list()
    regra.append(i.split('->')[0].strip())
    regra.append(i.split('->')[1].strip())
    regras.append(regra)
regrasDict = dict(regras)
    
print(axioma)
palavraAtual = axioma
for i in range (numeroDeExecucoes):
    novaPalavra = ''
    for j in palavraAtual:
        if j in regrasDict:
            novaPalavra += regrasDict[j]
        else:
            novaPalavra += j
    #print(novaPalavra)
    palavraAtual = novaPalavra

posicoes = list()
angulos = list()
pen = turtle.Pen()
pen.setheading(anguloInicial)
pen._tracer(25.0)
screen = turtle.Screen()
screen.screensize(10000,10000)
for i in palavraAtual:
    if i == 'F':
        pen.forward(5)
    elif i == '+':
        pen.left(angulo)
    elif i == '-':
        pen.right(angulo)
    if i == '[':
        posicoes.append(pen.position())
        angulos.append(pen.heading())

    if i == ']':
        pen.penup()
        pen.setpos(posicoes.pop())
        pen.setheading(angulos.pop())
        pen.pendown()
ts = turtle.getscreen().getcanvas()
canvasvg.saveall('lsystem.svg', ts)