D=int(input("Quantos dias o carro foi alugado? "))
Km=float(input('Quantos km você rodou com o carro?'))
VD=60
KMR=0.15
Valor=(D*VD)+(Km*KMR)
print('Você alugou o carro por {} dias e rodou {} KM, logo o valor a pagar pelo serviço é de R${:.2f}'.format(D,Km,Valor))
