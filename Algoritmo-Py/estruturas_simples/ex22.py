# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

areaAPintar = int(input('Digite a área em metros quadrados que voce deseja pintar'))
cadaLataPinta = 6
cadaLataCusta = 80

quantidadeAComprar = int(areaAPintar / cadaLataPinta)
quantidadeAPagar = quantidadeAComprar * cadaLataCusta

print('Voce deve comprar', quantidadeAComprar, 'latas, e o valor final será de', quantidadeAPagar, 'reais')
