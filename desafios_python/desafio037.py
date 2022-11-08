# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

n=int(input('Digite um número inteiro: '))
print('''Escolhas uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em BINÁRIO é {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(n, oct(n)[2:]))
elif opcao== 3:
    print('{} convertido em HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
    exit()