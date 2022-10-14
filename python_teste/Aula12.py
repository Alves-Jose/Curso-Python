nome=str(input('\033[35m Qual o seu nome?\033[m')).capitalize()
if nome=='Jose':
    print('Que lindo nome. Parabéns!')
elif nome=='Maria' or nome=='Pedro' or nome==('Paulo'):
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))