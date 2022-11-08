# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS '))
preço=float(input('Valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao=int(input('Qual a opção? '))
if opcao >4:
    print('Opção Inválida. Tente novamente.')
    exit()
if opcao==1:
    total= preço-(preço * 10/100)
elif opcao==2:
    total=preço-(preço * 5/100)
elif opcao==3:
    total=preço/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(total))
elif opcao==4:
    total=preço + (preço * 20/100)
    totparc= int(input('Quantas parcelas? '))
    parcela= total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
print('O valor das suas compras é R${:.2f} \n\033[1;32mValor total: R${:.2f}\033[m'.format(preço, total))

