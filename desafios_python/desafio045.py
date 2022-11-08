# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha=int(input('Qual a sua jogada? '))
random=random.randint(1,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('O computador escolheu {}'.format(random))
if escolha>3:
    print('Opção inválida. Tente novamente.')
    exit()
if escolha==random:
    print('EMPATE')
elif (escolha==1 and random==2) or (escolha==2 and random==3) or (escolha==3 and random==1):
    print('VOCÊ PERDEU!')
else:
    print('VOCÊ GANHOU!')

