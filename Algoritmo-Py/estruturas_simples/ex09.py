# 9 -  Cálculo de um salário líquido de um professor. Serão fornecidos valor da 
# hora aula, numero de aulas dadas e o % de desconto do INSS.

#INSS TABELA
#7,5% para quem ganha até um salário mínimo (R$ 1.212)
#9% para quem ganha entre R$ 1.212,01 e R$ 2.427,35
#12% para quem ganha entre R$ 2.427,36 e R$ 3.641,03
#14% para quem ganha entre R$ 3.641,04 e R$ 7.087,22.

valor_hora = float(input('Digite o valor da hora da sua aula'))
numero_aulas = int(input('Digite a quantidade de aulas que voce deu'))
hora_aula = int(input('Digite a quantidade de horas que cada aula que voce deu teve'))
salario = int(valor_hora * hora_aula * numero_aulas)
if salario <= 1212 :
        inss = 0.075
elif salario > 1212 and salario <= 2427.35 :
        inss = 0.09
elif salario > 2427.35 and salario <= 3641.03 :
        inss = 0.12
elif salario > 3641.03 and salario <= 7087.22 :
        inss = 0.14
elif salario > 7087.22 :
        inss = 0
print('O inss que vai incidir no seu salário é', inss, 'e o seu salário líquido é', salario - inss) 

