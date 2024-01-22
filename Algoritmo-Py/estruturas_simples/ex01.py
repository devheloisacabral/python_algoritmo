# 1- ) Fazer um programa que imprima a média aritmética dos números 8,9 e 7. 
# A média dos números 4, 5 e 6. A soma das duas médias. A média das 
# medias.

print('Média Aritmética')
numeros = int(7+8+9)/3
print ("A média aritmética dos números 7 8 e 9 é", numeros)
numeros2 = int(4 + 5 + 6) / 3
print (" A média das valores 4, 5 e 6 é", numeros)
soma = int(numeros + numeros2)
print ('A soma das medias é', soma)
medias = int(soma) / 2
print ('A média das médias é', medias) 
