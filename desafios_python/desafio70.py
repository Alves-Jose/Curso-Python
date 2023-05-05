# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

namemin = ' '
min = 0
cont = 0
total = 0
k = 0
question = ' '
print('-'*6)
print('MARKET')
print('-'*6)

while True:
    product = str(input('Products name: '))
    price = float((input('Price: $')))
    cont += 1
    total += price

    if price > 1000:
        k += 1
    if cont == 1:
        min = price
        namemin = product
    else:
        if price < min:
            min = price
            namemin = product

    question = str(input('Want to continue shopping? [Y/N]')).strip().upper()[0]
    while question not in 'YN':
        question = str(input('Want to continue shopping? [Y/N]')).strip().upper()[0]
    if question == 'N':
        break
print(f'Total: ${total}. Product costing more than 1k: {k}. The cheapest product was {namemin} and it costs $ {min}')