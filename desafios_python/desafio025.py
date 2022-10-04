nome=str(input('Qual o seu nome? ')).title().strip()
# print(nome[::].upper()=='Silva')
print('Seu nome tem Silva? {}'.format('Silva'in nome))
