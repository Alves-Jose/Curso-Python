snack = ('Burguer', 'Juice', 'Pizza', 'Pudim', 'French fries')

for cont in range(0, len(snack)):
    print(f'I will eat {snack[cont]} in position {cont}')

print('-'*10)

for food in snack:
  print(f'I will eat {food}')


print('-'*10)

for pos, food in enumerate(snack):
   print(f'I will eat {snack[cont]} in position {cont}')

print('I eat so much')