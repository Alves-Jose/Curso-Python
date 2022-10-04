salario=float(input('Salário total:R$'))
aumento=salario +(salario*15/100)
print('Seu salário antes era:R$ {:.2f} \nCom o aumento ficou:R$ {:.2f}'.format(salario, aumento))

#---Exercício Extra---

# valor=float(input('O valor é:R$'))
# desconto=valor -(valor*15/100)
# juros=valor +(valor*5/100)
# print('O valor do produto é:R${} \nPagamentos à vista ganha 15% de desconto, ficando apenas:R${} \nPagamentos parcelados têm juros mensal de 5%, ficando:R$ {}'.format(valor, desconto, juros))