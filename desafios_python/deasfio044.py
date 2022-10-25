# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco=float(input('Qual o valor do produto? R$'))
pag=str(input('Qual sua forma de pagamento? '))
pix=preco*10/100
desc_pix=preco-pix
if pag in 'Dinheiro Pix Cheque':
    print('O valor do seu produto é {} \nA forma de pagamento escolhida foi {} \nVocê ganhou R${:.2f} de desconto \nO valor final da sua compra é R${}'.format(preco, pag, pix, desc_pix))