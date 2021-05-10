# Programa em python para desenhar a espiral da sequencia
# fibonacci mostrando seus
# elementos
import turtle
import math


def fiboturtle(interacao):
    a = 0
    b = 1
    auxiliar_a = a
    auxiliar_b = b

    # Escolhendo a cor vermelho para desenhar os quadrados
    x.pencolor("red")

    # Desenhando o primeiro quadrado
    x.forward(b * multiplicador)
    x.left(90)
    x.forward(b * multiplicador)
    x.left(90)
    x.forward(b * multiplicador)
    x.left(90)
    x.forward(b * multiplicador)

    # Utilizando o algoritmo correspondente a sequencia
    # fibonacci para continuar o programa
    temp = auxiliar_b
    auxiliar_b = auxiliar_b + auxiliar_a
    auxiliar_a = temp

    # Desenhando o restante dos quadrados
    for i in range(1, interacao):
        x.backward(auxiliar_a * multiplicador)
        x.right(90)
        x.forward(auxiliar_b * multiplicador)
        x.left(90)
        x.forward(auxiliar_b * multiplicador)
        x.left(90)
        x.forward(auxiliar_b * multiplicador)

        # Utilizando o algoritmo correspondente a sequencia
        # fibonacci para continuar o programa
        temp = auxiliar_b
        auxiliar_b = auxiliar_b + auxiliar_a
        auxiliar_a = temp

    # Esconhendo o ponto inicial para desenhar a espiral
    x.penup()
    x.setposition(multiplicador, 0)
    x.seth(0)
    x.pendown()

    # Escolhendo a cor preto para desenhar a espiral
    x.pencolor("black")

    # Desenhando a espiral
    x.left(90)
    for i in range(interacao):
        print(b)
        num = math.pi * b * multiplicador / 2
        num /= 90
        for j in range(90):
            x.forward(num)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# O multiplicador serve pra aumentar ou diminuir
# a escala dos quadrados, assim multiplicando
# o seu tamanho
multiplicador = 4

# Definindo o numero de interações
n = int(input('Digite no numero de interacoes (numero > 1): '))

# Desenhando a espiral e mostrando seus elementos
if n > 0:
    print("A serie fibonacci para", n, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fiboturtle(n)
    turtle.done()
else:
    print("O numero de interacoes precisa ser maior que zero")
