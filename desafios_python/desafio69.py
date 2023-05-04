#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
c_age = 0
c_mens = 0
c_wom = 0
gender = ' '
question = ' '
while True:
    print('-'*17)
    print('REGISTER A PERSON')
    print('-'*17)

    age = int(input('Age: '))
    if age >= 18:
        c_age += 1
        
    gender = str(input('Gender: [M/F] ')).upper().strip()[0]
    while gender not in 'MF':
        gender = str(input('Gender: [M/F] ')).upper().strip()[0]
    if gender == 'M':
        c_mens = c_mens + 1
    if gender == 'F' and age < 20:
        c_wom = c_wom + 1
    print('-'*43)
    question = str(input('Do you want to register someone else? [Y/N] ')).upper().strip()[0]
    while question not in "YN":
        question = str(input('Do you want to register someone else? [Y/N] ')).upper().strip()[0]
    if question == "N":
        print(f'{c_age} People are over 18 years old. {c_mens} Men were registered. {c_wom} Women are under 20 years old')
        break
    print('-'*43)