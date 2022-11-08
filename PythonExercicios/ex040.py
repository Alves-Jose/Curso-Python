# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
media=(n1+n2)/2
if media<5.0:
    print('Sua média é {} e está abaixo de 5.0 pontos. \033[1;31mVocê está reprovado!\033[m'.format(media))
elif media >= 5 and media <7:
    print('Sua média é {} e está entre 5.0 e 6.9 pontos. \033[1;33mVocê está em recuperação`\033[m'.format(media))
elif media>=7:
    print('Sua média é {}. \033[1;32mParabéns! Você está aprovado.\033[m'.format(media))