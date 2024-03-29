Real=float(input('Qual o valor que você qer converter? : R$'))
Dolar=Real/5.02
Euro=Real/5.42
Libra=Real/6.34
print('Com o valor R${:.2f} você pode comprar US${:.2f}, ou €{:.2f} ou £ {:.2f} '.format(Real,Dolar,Euro, Libra))