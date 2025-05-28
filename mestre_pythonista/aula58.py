from turtle import Turtle
#inicializar turtle
t = Turtle()
#definir a velocicade
t.speed(1)

def obter_distancia():
    resposta = int(input('Quantos Pixels para frente? '))
    return resposta

def rotacionar_turtle(turtle)
   movimentar_para_lado = str(input('Rotacionar para d:direita, e:esquerda n:não rotacionar'))
       
def rotacionar_para_direita():
    

while True:
    direcao = str(input('Para qual direção devemos ir? F = Frente e T = Trás '))

    if direcao == 'F':
        distancia = int(input('Quantos Pixels para frente? '))
        rotacionar_turtle(t)

        rotacao = str(input('Rotacionar para d:direita, e:esquerda n:não rotacionar - '))
       
        if rotacao == 'd':
            angulo = int(input('Quantos pixels para a direita devemos rotacionar? '))
            t.right(90)
            t.forward(angulo)
        
        if rotacao == 'e':
            angulo = int(input('Quantos pixels para a esquerda devemos rotacionar? '))
            t.left(90)
            t.forward(angulo)
        
    if direcao == 'T':
        distancia = int(input('Quantos pixels para trás? '))
        t.backward(distancia)

        rotacao = str(input('Rotacionar para d:direita, e:esquerda n:não rotacionar - '))

        if rotacao == 'd':
            angulo = int(input('Quantos pixels para a direita devemos rotacionar? '))
            t.right(90)
            t.forward(angulo)
        
        if rotacao == 'e':
            angulo = int(input('Quantos pixels para a esquerda devemos rotacionar? '))
            t.left(90)
            t.forward(angulo)
        

    continuar = input('Continuar andando? ')
    if continuar not in ('Sim', 's'):
        break