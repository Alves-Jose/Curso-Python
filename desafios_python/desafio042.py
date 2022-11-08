# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-'*20)
print('Analisador de Triângulos')
print('-'*20)
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo ',end='')
    if r1== r2== r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1: 
        print('Escaleno')
    else: 
        print('Isósceles')
else: 
    print('As retas não podem formar um triângulo')