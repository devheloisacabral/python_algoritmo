# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: . salário bruto. a. quanto pagou ao INSS. b. quanto pagou ao sindicato. c. o salário líquido. d. calcule os descontos e o salário líquido, conforme a tabela abaixo: e. + Salário Bruto : R$ f. - IR (11%) : R$ g. - INSS (8%) : R$ h. - Sindicato ( 5%) : R$ = Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

salarioHora = float(input('Quanto vale a sua hora de trabalho?'))
horasTrabalhadas = float(input('Quantas horas voce trabalha por mes?'))

salario = salarioHora * horasTrabalhadas

impostoDeRenda = (salario * 0.11)
impostoDeRendaConvert = (salario * 0.11) - salario
INSSConvert = (salario * 0.08) - salario
INSS = (salario * 0.08)
sindicato = (salario * 0.05)
sindicatoConvert = (salario * 0.05) - salario
descontos = int(sindicato + INSS + impostoDeRenda)

salarioLiquido = salario - descontos

print('Salario bruto de', salario)
print('Voce pagou ao inss', INSS, 'reais')
print('Voce pagou', sindicato, 'reais ao sindicato')
print('Seu salario líquido foi de', salarioLiquido, 'reais')
