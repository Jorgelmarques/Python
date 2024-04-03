N1 = int (input('Digite Um Número : '))
N2 = int (input('Digite Outro Número: '))
if N1>N2:
    print('O número \033[31;42m{}\033[m é maior que o Número \033[31;42m{}\033[m' .format(N1,N2))
elif N1<N2:
    print('O número \033[31;42m{}\033[m é menor que o Número \033[31;42m{}\033[m'.format(N1,N2))
else:
    N1=N2
    print('O Número \033[31;42m{}\033[m e o Número \033[31;42m{}\033[m são iguais' .format(N1,N2))