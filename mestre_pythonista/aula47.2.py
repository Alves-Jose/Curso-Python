from turtle import Turtle
#inicializar turtle
t = Turtle()
#definir a velocicade
t.speed(1)
while True:
    direcao = str(input('Para qual direção devemos ir? F = Frente e T = Trás '))

    if direcao == 'F':
        direcao = int(input('Quantos Pixels para frente? '))
        direcao = t.forward(direcao)
        
    
    else:
        direcao = int(input('Quantos Pixels para trás? '))
        direcao = t.backward(direcao)

