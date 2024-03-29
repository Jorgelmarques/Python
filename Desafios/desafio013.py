Salário=float(input('Salárioi do Funcionário: R$'))
Reajuste=float(input('Qual o percentual do aumento'))
Novo=Salário + (Salário*Reajuste/100)
print("Com o reajuste de {:.2f}% o novo salário ficará em R${:.2f}" .format(Reajuste,Novo))
