salario=float(input('Digite seu salário atual:R$ '))
if salario<=1250:
    aumento=salario+(salario*15/100)
else:
     aumento=salario+(salario*10/100)
print('Seu salário de acordo com o aumento ficou:R${:.2f}'.format(aumento))
