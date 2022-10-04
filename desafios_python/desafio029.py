
#  Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado. -A multa vai custar R$7,00 por cada Km acima do limite.

km=int(input('Quantos km/h? '))
if km>80:
    print('Você está acima da velocidade permitida. Você foi multado!')
    m=(km-80)*7.00
    print('O valor da multa será:R${:.2f}'.format(m))
else: 
    print('Parabéns! Você dirige com cuidado.')