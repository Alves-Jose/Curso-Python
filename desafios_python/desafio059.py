
from time import sleep
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
opção=0
while opção != 5:
    print('O que você deseja fazer com esses valores?')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção=int(input('Qual a sua opção? '))
    if opção==1:
        soma=n1+n2
        print('A soma dos números {} e {} é {}'.format(n1, n2, soma))
    elif opção==2:
        mult=n1*n2
        print('A multiplicação dos números {} e {} é {}'.format(n1, n2, mult))
    elif opção==3:
        if n1>n2:
            print('O número maior é: {}'.format(n1))
        else:
            print('O número maior é: {}'.format(n2))
    elif opção==4:
        print('Informe os números novamente:')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif opção==5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
print('Fim do programa. Volte sempre!')