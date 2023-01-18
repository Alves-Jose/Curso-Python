# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# from random import randint
# n = 1
# num = 1
# while n != num:
#     n=int(input('Advinhe um número de 0 a 10: '))
#     num=randint(0, 10)
#     print('O número sorteado foi: {}'.format(num))
#     if num==n:     
#         print('Parabéns! Você ganhou <3 e teve {} tentativas'.format(num))
#     else:
#         num += 1
#         print('Infelizmente não foi dessa vez :(')

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print( 'Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    if jogador > computador:
        print('É menos...')
    if jogador < computador:
        print('É mais...')
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou! Seu número de tentativas foi {}'.format(palpites))
        