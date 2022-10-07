# tb=int(input('Peça uma tabuada:'))
# print('A tabuada é:')
# zero=tb*0
# um=tb*1
# dois=tb*2
# tres=tb*3
# quatro=tb*4
# cinco=tb*5
# seis=tb*6
# sete=tb*7
# oito=tb*8
# nove=tb*9
# dez=tb*10
# print('{} x 0 = {}'.format(tb, zero))
# print('{} x 1 = {}'.format(tb, um))
# print('{} x 2 = {}'.format(tb, dois))
# print('{} x 3 = {}'.format(tb, tres))
# print('{} x 4 = {}'.format(tb, quatro))
# print('{} x 5 = {}'.format(tb, cinco))
# print('{} x 6 = {}'.format(tb, seis))
# print('{} x 7 = {}'.format(tb, sete))
# print('{} x 8 = {}'.format(tb, oito))
# print('{} x 9 = {}'.format(tb, nove))
# print('{} x 10 = {}'.format(tb, dez))

num=int(input('\033[1;32m Peça uma tabuada: \033[m'))
print('\033[1;32m-\033[m'*12)
print('\033[1;35m{} x {:2} = {}'.format(num, 1, (num*1)))
print('{} x {:2} = {}'.format(num, 2, (num*2)))
print('{} x {:2} = {}'.format(num, 3, (num*3)))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {} = {}\033[m'.format(num, 10, num*10))
print('\033[1;32m-\033m'*12)