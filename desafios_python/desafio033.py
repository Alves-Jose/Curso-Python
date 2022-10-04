n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número: '))
#Testando menor
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
#Testando maior
maior=1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O seu número menor é: {}\nO seu número maior é: {}'.format(menor, maior))