salario = int(input('Qual o salário:'))
aumento1 = salario + ((salario/100)*10)
aumento2 = salario + ((salario/100)*15)
#salario abaixo de R$1.250
if salario < 1250:
    print('Seu salário de R${} receberá um aumento de 15%  e passará a ser de {}'.format(salario,aumento2))
#salario aacima de R$1.250
else:
    print("Seu salário de R${} receberá um aumento de 10% e passará a ser de R${}" .format(salario,aumento1))
