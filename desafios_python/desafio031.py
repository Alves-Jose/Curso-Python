km=float(input('Digite a distância da sua viagem: '))
print('Você está prestes a iniciar uma viagem de {}km'.format(km))
if km<=200:
    r=km*0.50
    print('O valor da sua viagem será de R${:.2f}'.format(r))
else:
    r2=km*0.45
    print('O valor da sua viagem será de R${:.2f}'.format(r2))