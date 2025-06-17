#criar listas usando loop e range
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

#Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    return nome + ' APROVADO'
    
print(list(map(aprovar_pessoa, nomes)))