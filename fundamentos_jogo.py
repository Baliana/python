import turtle
import time

tela = turtle.Screen()
tela.title("Eventos")
tela.bgcolor("white")
tela.setup(width=800, height=600)
tela.tracer(0)  # travamos as animações

def andar():
    jogador.forward(10)

def voltar():
    jogador.backward(10)

def virar_direita():
    jogador.setheading(jogador.heading() + 5)

def virar_esquerda():
    jogador.setheading(jogador.heading() - 5)

def crescer_taruga():
    jogador.shapesize(1.75, 1.75)
    jogador.write("Nhom Nhom Nhom!", move=False)

# Instanciando o jogador
jogador = turtle.Turtle()
jogador.shape("turtle")
jogador.shapesize(1.5, 1.5)

# Criando um obstáculo (alface)
alface = turtle.Turtle()
alface.color('green')
alface.shape('circle')
alface.penup()
alface.goto(300, 250)

# tela agora rastreia os cliques e teclas pressionadas
tela.listen()
tela.onkeypress(key='w', fun=andar)
tela.onkeypress(key='s', fun=voltar)
tela.onkeypress(key='a', fun=virar_direita)
tela.onkeypress(key='d', fun=virar_esquerda)

jogo_rodando = True
while jogo_rodando:
    time.sleep(0.015)  # ~60 fps
    tela.update()

    # colisão com a alface
    if jogador.distance(alface) <= 30:
        print('nhom nhom nhom')
        crescer_taruga()
        alface.goto(1000, 1000)

    # colisão com bordas da tela (limites de x e y)
    if jogador.xcor() >= 390:
        print('Ouch, bati na parede da direita!')
        jogador.setx(390)
    if jogador.xcor() <= -390:
        print('Ouch, bati na parede da esquerda!')
        jogador.setx(-390)
    if jogador.ycor() >= 290:
        print('Ouch, bati no teto!')
        jogador.sety(290)
    if jogador.ycor() <= -290:
        print('Ouch, bati no chão!')
        jogador.sety(-290)

tela.mainloop()
