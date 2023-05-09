# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-'*4)
print('BANK')
print('-'*4)


value = int(input('What the value? $'))
total = value
bal = 50
totbal = 0
while True:
    if total >= bal:
        total -= bal
        totbal += 1
    else:
        if totbal > 0:
            print(f'total of {totbal} ${bal} bills')
        if bal == 50:
            bal = 20
        elif bal == 20:
            bal = 10
        elif bal == 10:
            bal = 1
        totbal = 0
        if total == 0:
            break
print('-'*19)
print('Have a Good Day. :)')
