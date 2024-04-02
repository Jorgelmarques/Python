from math import hypot,sqrt
C1=float(input('Qual a medida do Cateto oposto ? :'))
C2=float(input('Qual a medida do Cateto adjacente ? :'))
H=hypot(C1,C2)
print('Com a medida do cateto oposto  {} e o cateto adjacente {} a hipotenusa tem a medida{:.2f}'.format(C1,C2,H))
C3=float(input('Qual a medida do cateto oposto? :'))
C4=float(input('Qual a medida do cateto adjacente? :'))
H1=(C3**2 + C4**2) **(1/2)
print('Com as medidas de Cateto oposto {} e Cateto adjacente {} teremos uma hipotenusa de {:.2f}' .format(C3,C4,H1))
