Preço=float(input('Qual o valor do Produto: R$'))
Desconto=float(input('Qual o percentual de desconto: '))
Final=Preço-(Preço*Desconto/100)
print('Com o desconto de{:.2f}% o seu produto custará R${:.2f}'.format(Desconto,Final))
