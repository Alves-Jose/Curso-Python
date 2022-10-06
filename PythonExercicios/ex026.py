frase=str(input('Digite uma frase:')).strip().upper()
print('A frase repete a letra "A" {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição:{}\nE aparece pela última vez  na posição:{}'.format(frase.find('A')+1, frase.rfind('A')+1))