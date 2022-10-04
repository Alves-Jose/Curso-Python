dias=int(input('Por quantos dias você alugou? '))
km=float(input('Quantos km foram percorridos? '))
dia=60*dias
rodado=0.15*km
total=dia+rodado
print('O total do seu aluguel é de: R${}'.format(total))