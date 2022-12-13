# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
tab=int(input('Digite uma tabuada: '))
for c in range(1,11):
   calc=tab*c
   print('{} x {:2} = {}'.format(tab, c, calc))
