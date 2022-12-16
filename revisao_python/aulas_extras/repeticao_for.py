percorrer uma lista
lista_produtos = ['faca','garfo', 'panela', 'frigideira', 'flavorstone']
for produto in lista_produtos:
    print(produto.capitalize())

#calcular o imposto sobre vários valores
lista_precos = [10,10,200,50,300]
for preco in lista_precos:
    imposto = preco * 0.1
    print(imposto)

#percorrendo um dicionário
produtos = { 
    'faca': 10,
    'garfo': 10,
    'panela': 200,
    'frigideira': 50,
    'flavorstone': 300,
}
for produto in produtos:
        print(produto)
        print(produtos[produto])

#RANGE
for _ in range(5):
    print('aaaa')

Análise de Vendas
in []: with open('vendasloja.txt','r') as arquivo:
texto = arquivo.read()
print(texto)