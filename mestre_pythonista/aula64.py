#dicionarios

'''
Pessoa
    nome
    idade
    altura
'''

pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]

#dicionario(chave, valor)
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
#pessoa_2 = dict(nome='Carol', idade=18, altura=1.60)

print(dicionario_pessoa.keys())
print(dicionario_pessoa.values())
print(dicionario_pessoa.items())

#iterar sobre um dicionario

for item in dicionario_pessoa.items():
    print(item[1])