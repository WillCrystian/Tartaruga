from turtle import Screen
from pista import Pista
from jogador import Jogador

tela =  Screen() # criar a tela
tela.setup(600,600) # tamanho da tela
tela.title('Tartaruga') 
tela.tracer(0)
tela.listen()

pista = Pista()
jogador = Jogador()

tela.onkey(jogador.mover_direita, 'Right')
tela.onkey(jogador.mover_esquerda, 'Left')

jogo_on = True

while jogo_on:
    tela.update()

tela.exitonclick()