#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n=int(input('Type a multiplication table: (Stop the program: -1)'))
    if n < 0:
        break
    for _ in range(1,11):
        calc = n * _
        print(f'{n} x {_} = {calc}')
print('End of the program. Welcome back anytime. Thank you!')