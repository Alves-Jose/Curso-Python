mostre=(input('\033[43m Tecle algo: \033[m'))
print('\033[1;35m O tipo primitivo deste valor é:\033[m \033[4;31m', type(mostre))
print('\033[1;35m É númerico?\033[m \033[4;31m', mostre.isnumeric())
print('\033[1;35m É alfabético?\033[m \033[4;31m', mostre.isalpha())
print('\033[1;35m É alfanumerico?\033[m \033[4;31m', mostre.isalnum())
print('\033[1;35m Só tem maíusculas?\033[m \033[4;31m', mostre.isupper())
print('\033[1;35m É um espaço?\033[m \033[4;31m', mostre.isspace())
print('\033[1;35m É impresso?\033[m \033[4;31m', mostre.isprintable())
print('\033[1;35m Está capitalizada?\033[m \033[4;31m', mostre.istitle())