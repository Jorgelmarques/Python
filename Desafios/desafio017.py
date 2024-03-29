from math import hypot
C1=float(input('Qual a medida do primeiro cateto? :'))
C2=float(input('Qual a medida do segundo cateto? :'))
H=hypot(C1,C2)
print('Com a medida do cateto oposto  {} e o cateto adjacente {} a hipotenusa tem a medida{}'.format(C1,C2,H))