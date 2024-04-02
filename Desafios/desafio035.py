print ("-=-"*20)
print ("Analisador de triângulos")
print ("-=-"*20)
r1 = float (input('Qual a medida do primeiro degmento?: '))
r2 = float (input('Qual a medida do segundo segmento?: '))
r3 = float (input("Qual a medida do Terceiro segmento?: "))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print("O segmentos acima podem formar um triângulo")
else:
    print("Com as medidas acima não podemos format um triângulo")
