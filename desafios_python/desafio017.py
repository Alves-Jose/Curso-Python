co=float(input('Digite o comprimento do Cateto Oposto: '))
ca=float(input('Digite o comprimento do Cateto Adjascente: '))
hi=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

import math 
co=float(input('Digite o comprimento do Cateto Oposto: '))
ca=float(input('Digite o comprimento do Cateto Adjascente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

