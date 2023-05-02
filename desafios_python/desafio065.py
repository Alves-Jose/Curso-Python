# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele 
# quer ou não continuar a digitar valores

r= 'S'
soma = qtd = media = maior = menor = 0
while r == 'S':
    n=int(input('Digite um valor: '))
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {}'.format(soma, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))