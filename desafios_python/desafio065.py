# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele 
# quer ou não continuar a digitar valores

r= 'S'
while r == 'S':
    n=int(input('Digite um valor: '))
    r=str(input('Quer continuar? [S/N] ')).upper()  
print('Fim')