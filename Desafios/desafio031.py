viagem=int(input('Qual a distacia da viagem: '))
km1=0.5*(viagem)
km2=0.45*(viagem)
if viagem<200:
    print ('a viagem vai custar:R${:.2f}'.format(km1))
else:
    print ('A viagem vai custar : R${:.2f}'.format(km2) )