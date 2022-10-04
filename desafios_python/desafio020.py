from random import shuffle
n1=str(input('Digite o nome: '))
n2=str(input('Digite o nome: '))
n3=str(input('Digite o nome: '))
n4=str(input('Digite o nome: '))
lista=[n1, n2, n3, n4]
sorteio=shuffle(lista)
print('A ordem da apresentação será')
print(lista)
