# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: "Qual o melhor Sistema Operacional para uso em servidores?" As possíveis respostas são: 1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte: Sistema Operacional Votos % ------------------- ----- --- Windows Server 1500 17% Unix 3500 40% Linux 3000 34% Netware 500 5% Mac OS 150 2% Outro 150 2% ------------------- ----- Total 8800 O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

votos = [0] * 7
while True:
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar")    
    voto = int(input("Digite o número correspondente ao seu voto: "))
    if 0 <= voto <= 6:
        votos[voto] += 1
    elif voto == 0:
        break
    else:
        print("Por favor, digite um número válido de 0 a 6.")
total_votos = sum(votos)
print("Sistema Operacional    Votos    %")
print("-------------------    -----    ---")
for i in range(1, 7):
    porcentagem = (votos[i] / total_votos) * 100
    print(f"{i}-", end=" ")
    if i == 1:
        print("Windows Server", end=" ")
    elif i == 2:
        print("Unix", end=" ")
    elif i == 3:
        print("Linux", end=" ")
    elif i == 4:
        print("Netware", end=" ")
    elif i == 5:
        print("Mac OS", end=" ")
    elif i == 6:
        print("Outro", end=" ")
    print(f"{votos[i]}    {porcentagem:.2f}%")

print("-------------------    -----    ---")
print("Total", total_votos)
vencedor_idx = votos.index(max(votos[1:]))
if vencedor_idx == 1:
    vencedor_nome = "Windows Server"
elif vencedor_idx == 2:
    vencedor_nome = "Unix"
elif vencedor_idx == 3:
    vencedor_nome = "Linux"
elif vencedor_idx == 4:
    vencedor_nome = "Netware"
elif vencedor_idx == 5:
    vencedor_nome = "Mac OS"
elif vencedor_idx == 6:
    vencedor_nome = "Outro"

print(f"O Sistema Operacional mais votado foi o {vencedor_nome}, com {votos[vencedor_idx]} votos, correspondendo a {porcentagem:.2f}% dos votos.")

