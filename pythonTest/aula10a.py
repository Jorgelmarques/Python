n1 = float (input('Digite a primeira nota:'))
n2 = float (input('Digite a Segunda nota : '))
n3 = float (input('Digite a terceira nota : '))
media= (n1+n2+n3)/3
if media>=6 :
    print('Muito bem sua nota final foi {:.2f}, e você foi aprovado' .format(media))
else:
    print('Sua média final foi {:.2f} e infelizmente você não foi aprovado' .format(media))
