# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} >'.format(termo), end='')
    termo += razao
    cont += 1
print('fim')
    