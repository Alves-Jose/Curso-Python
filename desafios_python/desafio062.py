
# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Digite a razão: '))
termo = primeiro
cont = 1
total=0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais?' ))
print('FIM')