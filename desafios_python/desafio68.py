#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-'*17)
print('EVEN OR ODD GAME')
print('-'*17)
cont = 0
while True:
    value = int(input('Your number: '))
    pc = randint(1, 10)
    total = value + pc
    pair = total % 2
    result = ' '
    while result not in 'EO':
        result = str(input('Even or Odd? [E/O] ')).upper().strip()
    
        if result == 'E':
            if pair == 0:
                print('Pair. You won')
                cont += 1
            elif pair != 0:
                print(f'Odd. You lose. You won {cont}')
                break

        elif result == 'O':
            if pair == 0:
                print(f'Pair. You lose. You won {cont}')
                break
                
            elif pair != 0:
                print('Odd. You won')
                cont += 1

    print('-'*37)
    print(f'Your number: {value} Pc number: {pc} Total: {total} ')
    print('-'*37)
    