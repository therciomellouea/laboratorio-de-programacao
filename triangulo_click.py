import turtle

# Obtendo a tela
tela = turtle.Screen()

# Criando o turtle
tart = turtle.Turtle()


def triangle(x, y):
    # Usado para parar de desenhar
    tart.penup()

    # Usado para mover o cursor para a pos X e Y
    tart.goto(x, y)

    # Usado para desenhar
    tart.pendown()
    for i in range(3):
        # Movendo o cursor 100 unidades
        tart.forward(100)

        # Virando o cursos 120 graus para a esquerda
        tart.left(120)

        # Movendo o cursor 100 unidades
        tart.forward(100)


# Funcao para mandar a posicao atual do cursor
# para o triangulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# Para que a tela nao feche ao iniciar o programa
turtle.done()
