num = (int (input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Mais um número: ')),
       int(input('Outro: ')))

print(f'Você digitou os números {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')

else:
    print('O número 3 não foi digitado')

for n in num:
    if n % 2 == 0:
        print(f'Os números pares são: {n}')