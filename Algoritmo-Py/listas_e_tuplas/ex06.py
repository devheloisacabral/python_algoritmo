# 6 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randint

resultado = [0] * 7   
for i in range(100):
    x = randint(1,6)
    resultado[x] += 1
    
for i in range(1, 7):
    print(i, ": ", resultado[i])
