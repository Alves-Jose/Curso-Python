# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma=0
cont=0
for com in range(1, 7):
    n=int(input('Digite o {} número: '.format(com)))
    if n % 2 ==0:
        soma=soma+n
        cont=cont+1
print('A soma dos {} pares é {}'.format(cont, soma))