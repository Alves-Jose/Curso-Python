#  Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador. -O programa deverá escrever na tela se o usúario venceu ou perdeu.

from random import randint
n=int(input('Advinhe um número de 0 a 5: '))
num=randint(0, 5)
print('O número sorteado foi: {}'.format(num))
if num==n:
    print('Parabéns! Você ganhou <3')
else:
    print('Infelizmente não foi dessa vez :(')