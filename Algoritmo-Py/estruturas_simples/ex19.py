# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: a. o produto do dobro do primeiro com metade do segundo . b. a soma do triplo do primeiro com o terceiro. c. o terceiro elevado ao cubo.

int1 = int(input('Digite um numero inteiro'))
int2 = int(input('Digite mais um numero inteiro'))
float1 = float(input('Agora, digite um número real'))

conta1 = (int1 * 2) * (int2 / 2) 
conta2 = int1 * 3 + float1
conta3 = float1 * float1 * float1

print('o produto do dobro do primeiro com metade do segundo é', conta1, 'a soma do triplo do primeiro com o terceiro é', conta1, 'e o terceiro numero elevado ao cubo é', conta3)
