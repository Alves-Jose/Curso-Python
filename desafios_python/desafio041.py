#  Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
nasc=int(input('Digite sua data de nascimento: '))
atual=date.today().year
idade=atual-nasc
if idade>=0 and idade<=9:
    print('Você têm {} anos. \033[1;32mSua categoria é MIRIM\033[m'.format(idade))
elif idade>=10 and idade <=14:
    print('Você têm {} anos. \033[1;32mSua categoria é INFANTIL\033[m'.format(idade))
elif idade>=15 and idade <=19:
    print('Você têm {} anos. \033[1;32mSua categoria é JUNIOR\033[m'.format(idade))
elif idade==20:
    print('Você têm {} anos. \033[1;32mSua categoria é SENIOR\033[m'.format(idade))
elif idade>21:
    print('Você têm {} anos. \033[1;32mSua categoria é MASTER\033[m'.format(idade))