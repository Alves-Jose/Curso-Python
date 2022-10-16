from datetime import date
sexo=str(input('Digite seu gênero: '))
if sexo in 'Feminino Mulher feminino mulher':
    print('Seu alistamento não é obrigatório')
    exit()
if sexo in 'Masculino Homem masculino homem':
    print('O seu alistamento é obrigatório')
    print('Continue preenchendo o formulário:')
else:
    print('Gênero inválido. Tente novamente.')
    exit()
nasc=int(input('Digite o ano do seu nascimento: '))
atual=date.today().year
idade=atual-nasc
print('Você têm {} anos'.format(idade))
if idade<18:
    saldo=18-idade
    print('Ainda faltam {} anos para você se alistar ao serviço militar'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade==18:
    print('Está na hora de se alistar ao serviço militar')
elif idade>18:
    saldo=idade-18
    print('O tempo do seu alistamento já passou {} anos'.format(saldo))
    ano=atual-saldo
    print('Seu alistamento foi em {}'.format(ano))