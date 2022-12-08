# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome

nome=str(input('Digite seu nome: ')).strip()
print('Seu nome é {}'.format(nome.title()))
print('Seu nome com todas as letras MAIÚSCULAS é: {}'.format(nome.upper()))
print('Seu nome com todas as letras MINÚSCULAS é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
sep=nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(sep[0].title(), len(sep[0])))