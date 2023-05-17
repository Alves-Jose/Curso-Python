# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    n = int(input('Enter a number from 0 to 20: '))
    if 0 <= n <= 20:
        break
    print('Try again.', end=' ')
print(f'You typed the number {cont[n]}')
