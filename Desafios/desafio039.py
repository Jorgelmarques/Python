from datetime import date
data = date.today()
anoatual = date.year
diaatual= date.day
mesatual=date.month
dia = int(input( 'Que dia você nasceu? '))
mes = int(input ( 'Que mes você nasceu? '))
ano = int(input( 'Que ano você nasceu?' ))
idade = date.year - ano


print( 'De acordo com meus calculos você tem:', int(anoatual) - int(ano), 'anos de idade' )