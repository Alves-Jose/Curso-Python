# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso=float(input('Digite seu peso(kg): '))
altura=float(input('Digite sua altura(m): '))
imc=peso/(altura**2)
if imc < 18.5:
    print('Seu peso é {}, sua altura é {:.2f} e seu IMC é {:.2f}. \033[1;31mVocê está abaixo do seu peso\033[m'.format(peso, altura, imc))
elif imc>= 18.5 and imc<= 25:
    print('Seu peso é {}, sua altura é {:.2f} e seu IMC é {:.2f}. \033[1;32mVocê está no peso ideal\033[m'.format(peso, altura, imc))
elif imc>= 25 and imc<= 30:
    print('Seu peso é {}, sua altura é {:.2f} e seu IMC é {:.2f}. \033[1;31mVocê está em sobrepeso.\033[m'.format(peso, altura, imc))
elif imc>= 30 and imc <= 40:
    print('Seu peso é {}, sua altura é {:.2f} e seu IMC é {:.2f}. \033[1;31mVocê está em Obesidade.\033[m'.format(peso, altura, imc))
elif imc> 40:
    print('Seu peso é {}, sua altura é {:.2f} e seu IMC é {:.2f}. \033[1;31mVocê está em Obesidade Morbida. \033[m'.format(peso, altura, imc))