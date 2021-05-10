from turtle import *

speed('fastest')

# Fazendo o turtle ir para cima
lt(90)

# O angulo agudo entre a base e a ramificacao
# de Y
angulo = 30


# Funcao para desenhar o Y
def desenha_y(tamanho, nivel):
    if nivel > 0:
        colormode(255)

        # Escolhendo a cor verde em intervalos iguais
        # para cada nivel, definindo a cor de acordo
        # com o nivel atual
        pencolor(0, 255 // nivel, 0)

        # Desenhando a base
        fd(tamanho)

        rt(angulo)

        # Chamada recursiva para o lado direito da arvore
        desenha_y(0.8 * tamanho, nivel - 1)

        pencolor(0, 255 // nivel, 0)

        lt(2 * angulo)

        # Chamada recursiva para o lado esquerdo da arvore
        desenha_y(0.8 * tamanho, nivel - 1)

        pencolor(0, 255 // nivel, 0)

        rt(angulo)
        bk(tamanho)


# tree of size 80 and level 7
desenha_y(80, 7)
