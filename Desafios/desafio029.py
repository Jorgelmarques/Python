Velocidade=int(input('Qual a velocidade do carro: '))
multa=7
pena =(Velocidade-80)*7
if Velocidade > 80:
    print('Você foi multado')
    print ('O valor da Multa é : {}'.format(pena))