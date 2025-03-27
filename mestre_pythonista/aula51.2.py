# def gerar_nome_completo(nome, sobrenome):
#     print(f'Olá, meu nome é {nome} e meu sobrenome é {sobrenome}')

# gerar_nome_completo('José Marcos', 'Pereira Alves')

def calcular_valores(preco, quantidade = 1):
    total = preco * quantidade
    print(f'O valor total é de R${total}')

calcular_valores(2.00, 2)