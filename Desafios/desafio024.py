cidade=str(input('Digite o Nome da sua Cidade:'))
separa=cidade.split()
print("A cidade {} tem a primeira palavra santo? {}".format(cidade,cidade[:5].upper() == 'SANTO'))
