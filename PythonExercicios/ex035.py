print('-'*25)
print('Analisador de Triângulos')
print('-'*25)

r1=float(input('Primeiro Segmento: '))
r2=float(input('Segundo Segmento: '))
r3=float(input('Terceiro Segmento: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Parabéns! As retas {}, {} e {} podem formar um triângulo'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} nao formam um triângulo :('.format(r1,r2,r3))