nome=str(input('Digite seu nome completo: ')).title().strip()
print('Olá, prazer em te conhecer {}'.format(nome))
p=nome.split()
print('Seu primeiro nome é {}\nSeu último nome é {}'.format(p[0],p[-1]))