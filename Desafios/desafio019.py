from random import choice
aluno1=str(input('Qual o nome do primeiro aluno?: '))
aluno2=str(input('Qual o nome do segundo aluno?: '))
aluno3=str(input('Qual o nome do terceiro aluno?: '))
aluno4=str(input('Qual o nome do quarto aluno?: '))
Inscritos = (aluno1 , aluno2 , aluno3 , aluno4)
sorteio = choice(Inscritos)
print('O resultado do sorteio foi {}' .format(sorteio))