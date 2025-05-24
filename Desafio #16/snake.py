import turtle as t
import time
import random

# Configuração da tela
tela = t.Screen()
tela.title("Super Cobra 9000 GTX FURY")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Cabeça da cobra
head = t.Turtle()
head.shape("square")
head.color('red')
head.penup()

segmentos = []

# Maçã
maca = t.Turtle()
maca.shape('circle')
maca.color('red')
maca.penup()
maca.goto(100, 0)

# Funções de movimento
def mover_cima():
    if head.heading() != 270:
        head.setheading(90)

def mover_baixo():
    if head.heading() != 90:
        head.setheading(270)

def virar_direita():
    if head.heading() != 180:
        head.setheading(0)

def virar_esquerda():
    if head.heading() != 0:
        head.setheading(180)

# Criar novo segmento
def criar_seguimento():
    novo = t.Turtle()
    novo.shape("square")
    novo.color("yellow")
    novo.penup()
    segmentos.append(novo)

# Teclado
tela.listen()
tela.onkeypress(mover_cima, "w")
tela.onkeypress(mover_baixo, "s")
tela.onkeypress(virar_direita, "d")
tela.onkeypress(virar_esquerda, "a")

# Loop principal
while True:
    tela.update()
    time.sleep(0.1)

    # Mover os segmentos do corpo
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        segmentos[0].goto(head.xcor(), head.ycor())

    head.forward(20)

    # Colisão com a maçã
    if head.distance(maca) < 20:
        print("Nhom Nhom Nhom!")
        criar_seguimento()
        x_random = random.randint(-380, 380)
        y_random = random.randint(-280, 280)
        maca.goto(x_random, y_random)

    # Colisão com bordas
    if abs(head.xcor()) > 390 or abs(head.ycor()) > 290:
        print("Bateu na parede! Reiniciando...")
        time.sleep(1)
        head.goto(0, 0)
        head.setheading(0)
        for seg in segmentos:
            seg.goto(1000, 1000)
        segmentos.clear()

    # Colisão com o próprio corpo
    for seg in segmentos[1:]:
        if head.distance(seg) < 20:
            print("Bateu em si mesma! Reiniciando...")
            time.sleep(1)
            head.goto(0, 0)
            head.setheading(0)
            for seg in segmentos:
                seg.goto(1000, 1000)
            segmentos.clear()
            break

tela.mainloop()