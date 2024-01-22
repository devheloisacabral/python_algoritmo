agenda = []


def salvar_agenda(): # padrao para enviar a lista maior para um arquivo externo txt
    with open('agenda.txt', 'w') as arquivo:
        for contato in agenda:
            arquivo.write(f"{contato['Nome']},{contato['Endereço']},{contato['Telefone']}\n")
    

 
def carregar_agenda(): #carrega agenda
    try:
        with open('agenda.txt', 'r') as arquivo:
            for linha in arquivo:
                nome, endereco, telefone = linha.strip().split(',')
                agenda.append({'Nome': nome, 'Endereço': endereco, 'Telefone': telefone})
        print("Agenda carregada com sucesso!")
    except FileNotFoundError:
        print("Arquivo da agenda não encontrado. Uma nova agenda vazia será criada.")


carregar_agenda()


def voltarAoMenu():  # feito
    escolha = input('Deseja voltar ao menu principal? S/N ')
    if escolha == 'S' or escolha == 's':
        menuPrinci()
    


def tela1():  # pega os dados e envia em forma de lista para uma lista
    print('\n#------------------------------------------------------#')
    print(' # 1 – CADASTRAR NOME #')
    print(' #------------------------------------------------------#')
    nome = input('Digite seu nome ')
    endereco = input('Digite seu endereço ')
    telefone = input('Digite seu telefone ')  # falta pegar os dados e transferir para uma lista de listas num arquivo externo
    agenda.append({'Nome': nome, 'Endereço': endereco, 'Telefone': telefone})
    salvar_agenda()
    voltarAoMenu()


def tela2():
    print('\n #------------------------------------------------------#')
    print('# 2 – CONSULTAR NOME #')
    print(' #------------------------------------------------------#')
    nome = input("Digite o nome a ser consultado: ")
    for contato in agenda:
        if contato['Nome'].lower() == nome.lower():
            print(f"Nome: {contato['Nome']}, Endereço: {contato['Endereço']}, Telefone: {contato['Telefone']}")

        else:
            print("Nome não encontrado na agenda.")  # preciso importar a lista externa para ca para conseguir dar um print na lista referente ao nome

    voltarAoMenu()


def tela3():  # tem que achar a lista como array na lista maior e apagar essa lista menor
    print('\n #------------------------------------------------------#')
    print('# 3 – EXCLUIR NOME #')
    print(' #------------------------------------------------------#')
    nome = input("Digite o nome a ser excluído: ")
    for contato in agenda:
        if contato['Nome'].lower() == nome.lower():
            agenda.remove(contato)
            print("Nome excluído com sucesso!")
        else:
            print("Nome não encontrado na agenda.")
    salvar_agenda()        
    voltarAoMenu()


def tela4():  # só listar todas as menores listas qe estão dentro de uma lista maior
    print('\n #------------------------------------------------------#')
    print('# 4 – LISTAR TODOS OS NOMES #')
    print(' #------------------------------------------------------#')
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['Nome']}, Endereço: {contato['Endereço']}, Telefone: {contato['Telefone']}")
            
    voltarAoMenu()


def tela5():  # apagar todos os dados da lista maior
    print('\n #------------------------------------------------------#')
    print('# 5 – ZERAR AGENDA ')
    print(' #------------------------------------------------------#')
    decisao = input('Deseja mesmo zerar todos os dados dessa agenda?')
    if decisao == 'S' or decisao == 's':
        agenda.clear()
        print("Agenda zerada com sucesso!")
    else:
        voltarAoMenu()
    salvar_agenda()      
    voltarAoMenu()


def tela6():  # feito
    desenvolvedores = ['Heloisa Coelho Cabral - 202311029']  #feito
    print('\n #------------------------------------------------------#')
    print('# 6 - DESENVOLVEDORES #')
    print(' #------------------------------------------------------#')

    print('Dev', desenvolvedores)
    voltarAoMenu()


def tela7():  # feito
    print('Esse programa foi encerrado')


def menuPrinci():  # feito
    print('\n #------------------------------------------------------#')
    print('# A G E N D A D E E N D E R E Ç O S #')
    print('#------------------------------------------------------#')
    print('\n# OPÇÕES #')
    print('\n# 1 – CADASTRAR NOME #')
    print('# 2 – CONSULTAR NOME #')
    print('# 3 – EXCLUIR NOME #')
    print('# 4 – LISTAR TODOS OS NOMES #')
    print('# 5 – ZERAR AGENDA ')
    print('# 6 - DESENVOLVEDORES #')
    print('# 7 – SAIR #')
    print('#------------------------------------------------------#')
    valor = int(input((' # DIGITE A OPÇÃO DESEJADA (1 A 7): ')))
    if valor == 1:
        tela1()
    if valor == 2:
        tela2()
    if valor == 3:
        tela3()
    if valor == 4:
        tela4()
    if valor == 5:
        tela5()
    if valor == 6:
        tela6()
    if valor == 7:
        tela7()


menuPrinci()
salvar_agenda()
