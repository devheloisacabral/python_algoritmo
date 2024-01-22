# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. o C = (5 * (F-32) / 9).

fa = float(input('Digite uma temperatura em graus  Farenheit '))
celsiu = (5*(fa-32)/9)

print('Essa temperatura em graus celsius é de', celsiu)
