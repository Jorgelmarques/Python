cores = {'limpa':'\033[m',
         'azulfpreto':'\033[34;40m',
         'amafverd':'\033[33;42m',
         'pb': '\033[7;30m'}
print('\033[34;40m-=-\033[m'*10)
print('\033[34;40mEmpréstimo Bancário\033[m')
print('\033[34;40m-=-\033[m'*10)
Valor = float(input('Qual o Valor do Imóvel: R$ '))
Salario = float(input('Qual o Seu Salário: R$ '))
Idade = float(input('Qual a sua Idade? : '))
TF = float(input('Por Quantos anos você quer Financiar o Imóvel? : '))
Prestação = Valor / (TF*12)
print('Para o valor de \033[31;42mR${:.2f}\033[m  e pagar em \033[31;42m{:.0f}\033[m meses\n a prestação ficará em \033[31;42mR${:.2f}\033[m'.format(Valor,TF,Prestação))
if Prestação > (Salario*0.30):
    print('Infelizmente seu empréstimo foi \033[31;43mNEGADO\033[m' )
else:
    print('Seu empréstivo foi \033[31;43mAPROVADO\033[m e poderemos dar andamento no processo')


