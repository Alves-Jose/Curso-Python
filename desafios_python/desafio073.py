# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense

times = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Internacional', 'Cruzeiro', 
'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense',
'Vitória')

print(times)

for cont in range(0, 5):
    print(times[cont])

print(times[-4:])

print(sorted(times))

print(times.index('Fluminense')+1)