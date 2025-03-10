from datetime import datetime

# print(datetime.now())
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().year)

# #criar uma data
# lancamento_app = datetime(2021, 5, 28)
# print(lancamento_app)
# #quero receber a data de lançamento do meu app%m
# data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'),'%d/%m/%Y')
# print(data_de_lancamento)

# data_atual = datetime.now()
# prazo = data_de_lancamento - data_atual
# print(prazo.days)

data_atual = datetime.now()

data_aniversario = data_atual.strptime(input('Digite sua data de aniversário:'), '%d/%m/%Y')
print(data_aniversario)

dias_restantes = data_atual - data_aniversario
print(dias_restantes.days)