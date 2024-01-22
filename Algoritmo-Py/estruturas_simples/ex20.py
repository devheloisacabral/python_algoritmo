# 13. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: . Para homens: (72.7*h) - 58 a. Para mulheres: (62.1*h) - 44.7 (h = altura) b. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

altura = float(input('Digite sua altura em metros'))
sexo = input('Digite seu sexo')

pesoIdealHomem = 72.7 * altura - 58
pesoIdealMulher = 62.1 * altura - 44.7

if sexo == 'masculino' : 
    print('Seu peso ideal é', pesoIdealHomem, 'kg')
elif sexo == 'feminino' : print('Seu peso ideal é', pesoIdealMulher)
