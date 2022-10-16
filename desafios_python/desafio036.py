valor=float(input('Qual o valor da casa? R$'))
salário=float(input('Você pode me informar o seu salário? R$'))
anos=int(input('Em quantos anos você deseja pagar?'))
prestacão=valor/(anos*12)
mínimo=salário*30/100
if prestacão>mínimo:
    print('Para pagar uma casa de R${:.0f} em {} anos a prestação será de {:.2f}'.format(valor, anos, prestacão))
    print('\033[1;31mEmpréstimo negado!\033[m')
else:
    print('Para pagar uma casa de R${:.0f} em {} anos a prestação será de {:.2f}'. format(valor, anos, prestacão))
    print('\033[1;32mEmpréstimo aprovado!\033[m')
