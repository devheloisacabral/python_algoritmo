# 13 - Ler 1 número. Se positivo, imprimir raiz quadrada senão o quadrado.

numero =  float(input('Digite um número qualquer'))
if numero >= 0:
    print('A raiz quadrada do seu número é', int(numero **0.5))
else:
    print('Nada acontece pois o número que voce digitou é negativo')
