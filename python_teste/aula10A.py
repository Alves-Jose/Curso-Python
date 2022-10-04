# nome=str(input('Qual o seu nome? '))
# if nome=='José':
#     print('Que nome lindo você tem! xD')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}'.format(nome))

print('----- Vamos calcular sua média? -----')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print('A sua média foi: {}'.format(m))
if m>=6.0:
    print('Parabéns pela sua nota! :)')
else:
    print('Você não passou. Se esforce mais da próxima vez. :(')
