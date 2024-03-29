Largura=float(input('Qual a largura da sua parede?'))
Altura=float(input('Qual a altura da sua parede?'))
Area=Largura*Altura
Tinta=Area/2
print('Com a largura {}m  e a altura {}m, você tem a área da sua parede é de {:.2f}'.format(Largura,Altura,Area))
print('Para pintar a sua parede você vai gastar {:.2f}l de tinta'.format(Tinta))

