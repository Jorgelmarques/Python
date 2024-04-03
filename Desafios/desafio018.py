from math import radians,sin, cos, tan
Ângulo=float(input('Digite um ângulo:'))
seno = sin(radians(Ângulo))
coseno=cos(radians(Ângulo))
tangente=tan(radians(Ângulo))
print('O ângulo de {}° tem o SENO de{:.2f}'.format(Ângulo,seno))
print('O ângulo de {}° tem seu COSENO de {:.2f}' .format(Ângulo,coseno))
print('O ângulo de {}° tem sua tangente no valor de {:.2f}'.format(Ângulo,tangente))