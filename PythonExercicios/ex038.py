n1=int(input('Escreva um número: '))
n2=int(input('Escreva outro número '))
if n1>n2:
    print('\033[1;32mO primeiro valor é maior\033[m')
if n2>n1:
    print('\033[1;32mO segundo valor é maior\033[m')
if n1==n2:
    print('\033[1;32mNão existe valor maior, os dois são iguais\033[m')