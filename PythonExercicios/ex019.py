# import random
# nome1=str(input('Digite o nome: '))
# nome2=str(input('Digite o nome: '))
# nome3=str(input('Digite o nome: '))
# nome4=str(input('Digite o nome: '))
# escolhido=random.choice(nome1, nome2, nome3, nome4)
# print('O escolhido foi: {}'.format(escolhido))


# import random
# n1=str(input('Digite o nome: '))
# n2=str(input('Digite o nome: '))
# n3=str(input('Digite o nome: '))
# n4=str(input('Digite o nome: '))
# lista=[n1, n2, n3, n4]
# sorteio=random.choice(lista)
# print('O escolhido foi: {}'.format(sorteio))

from random import choice
n1=str(input('Digite o nome: '))
n2=str(input('Digite o nome: '))
n3=str(input('Digite o nome: '))
n4=str(input('Digite o nome: '))
lista=[n1, n2, n3, n4]
sorteio=choice(lista)
print('O escolhido foi: {}'.format(sorteio))