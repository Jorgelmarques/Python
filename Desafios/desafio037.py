Numero = int ( input ('Digite um número inteiro :'))
print('''Escolha uma das 3 bases de conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção=int(input('Sua Opção:'))
if opção ==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(Numero,bin(Numero)[2:]))
elif opção ==2:
    print('{} convertido para OCTAL é igual a {}' .format(Numero,oct(Numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(Numero,hex(Numero)[2:]))
else:
    print('Opção Inválida, tente Novamente')