# 3.Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre: . O modelo do carro mais econômico; a. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

modelos = []
consumos = []

for i in range(1, 6):
    print('Veículo %d' % i)
    modelos.append(input('Nome: '))
    consumos.append(float(input('Km por litro: ')))

print('Relatório Final')
cont, custo = 0, 0
gasto = 0
menorModelo = ''
menor = 0
for m in modelos:
    custo = 1000 / consumos[cont]
    gasto = custo * 2.25
    print('%s      - %.1f  -  %.1f litros  - R$ %.2f' % (m, consumos[cont], consumos, gasto))
    if cont == 0:
        menor = custo
        menorModelo = m
    if menor < custo:
        menor = custo
        menorModelo = m
    cont += 1
print('O menor consumo é do %s.' % (menorModelo))
