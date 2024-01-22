alunos = {}  #Lista para armazenar cada aluno do codigo

while True: #loop enquanto as opções forem verdadeiras #será quebrado no break no final do código
    print("\n \n \t \t \t Cadastro de Alunos: ")
    print("1. Incluir")
    print("2. Consultar/Alterar")
    print("3. Excluir")
    print("4. Listar Alunos")
    print("5. Sair do programa")
    
    opcao = input("Escolha uma opção entre 1 e 5 para acessar o sistema: ")

    if opcao == "1":
        print(" \n \n \t \t \t Inclusão de Novos Alunos")
        matricula = input("\n \n Matrícula: ")
        while matricula in alunos:
            print("Essa matrícula já está cadastrada no sistema. Por favor, infome uma matrícula válida.")
            matricula = input("Matrícula: ")
        
        nome = input("Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2) / 2
        print(nome, "- A sua média é ", media)

       
        incluir = input("Deseja incluir o aluno (S/N)? ")
        if incluir.lower() == 's':
            alunos[matricula] = {'Nome': nome, 'Nota1': nota1, 'Nota2': nota2, 'Média': media} #[] puxa a lista e os atributos de dentro dela 
            print('O aluno foi cadastrado. Você será direcionado ao menu principal')
        elif incluir.lower() == 'r':
            continue
        else:
            print('Procedimento cancelado. Retorne ao menu principal')

    elif opcao == "2":
        print("\n \n \t \t \tConsulta e Alteração de Aluno")
        matricula = input("Matrícula: ")
        if matricula in alunos:
            aluno = alunos[matricula]
            print(f'Nome: {aluno["Nome"]}')
            print(f'Nota 1: {aluno["Nota1"]}')
            print(f'Nota 2: {aluno["Nota2"]}')
            print(f'Média: {aluno["Média"]:.2f}')
            alterarAluno = input("Deseja alterar os dados do aluno (S/N)? ")
            if alterarAluno.lower() == 's':
                nome = input("Informe o novo Nome que deseja inserir: ")
                nota1 = float(input("Informe uma nova Nota 1: "))
                nota2 = float(input("Informe uma nova Nota 2: "))
                media = (nota1 + nota2) / 2
                alunos[matricula] = {'Nome': nome, 'nota1': nota1, 'nota2': nota2, 'Média': media}
                print('Ok! Os dados do aluno foram atualizados com sucesso!')
            elif alterarAluno.lower() == 'r':
                continue
        else:
            print('A matrícula informada não foi encontrada no banco de dados. Por favor, digite uma matrícula válida.')

    elif opcao == "3":
        print("\n \n \t \t \t Exclusão")
        matricula = input("Matrícula: ")
        if matricula in alunos:
            excluirAluno = input("Deseja excluir o aluno que diz respeito a essa matrícula (S/N)? ")
            if excluirAluno.lower() == 's':
                del alunos[matricula]
                print('O Aluno foi exlcuído do sistema com sucesso!')
            elif excluirAluno.lower() == 'r':
                continue
        else:
            print('Essa matrícula não consta no banco de dados. Informe uma matrícula válida')

    elif opcao == "4":
        print("\n \n \t \t \tListagem de alunos cadastrados")
        if alunos:
            print("Alunos:")
            for matricula, aluno in alunos.items():
                 print(f"Matrícula: {matricula}, \t Nome: {aluno['Nome']},\t Média: {aluno['Média']:.2f}")
        else:
            print(" \n \n Nenhum aluno foi cadastrado nesse sitema ainda. Favor, cadastre um aluno na opção 1 do MENU.")
            
    elif opcao == "5":
        print("\n \n Você saiu do sistema. O programa será finalizado.")
        break

    else:
        print("Opção inexistente no menu principal. Digite uma opção entre 1 e 5 ")

# o true fica false e o programa para