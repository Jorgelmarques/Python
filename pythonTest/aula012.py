nome=str(input('Qual o seu nome?'))
if nome=='Gustavo':
    print('Que Nome Bonito')
elif nome=='Jorge' or nome=='Juliana' or nome=='Marcelo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem Normal')
print('Tenha um bom dia, {}!'.format(nome))