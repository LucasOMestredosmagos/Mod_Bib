alunos = {}

def AdicionarAluno(matricula, nome, curso):
    alunos[matricula] = {"nome": nome, "curso": curso}
    print(f"\033[92mAluno {nome} adicionado com sucesso!\033[0m")

def RemoverAluno(matricula):
    if matricula in alunos:
        del alunos[matricula]
        print(f"\033[91mAluno com matrícula {matricula} removido com sucesso!\033[0m")
    else:
        print(f"\033[93mAluno com matrícula {matricula} não encontrado!\033[0m")

def AtualizarAluno(matricula, nome=None, curso=None):
    if matricula in alunos:
        if nome:
            alunos[matricula]["nome"] = nome
        if curso:
            alunos[matricula]["curso"] = curso
        print(f"\033[92mAluno com matrícula {matricula} atualizado com sucesso!\033[0m")
    else:
        print(f"\033[93mAluno com matrícula {matricula} não encontrado!\033[0m")

def ListarAlunos():
    print("\033[94m=> Lista de alunos <=\033[0m")
    for matricula, aluno in alunos.items():
        print(f"\033[96mMatrícula: {matricula}, Nome: {aluno['nome']}, Curso: {aluno['curso']}\033[0m")

while True:
    print("\033[94mOpções:\033[0m")
    print("\033[96m1. Adicionar aluno\033[0m")
    print("\033[96m2. Remover aluno\033[0m")
    print("\033[96m3. Atualizar aluno\033[0m")
    print("\033[96m4. Listar alunos\033[0m")
    print("\033[96m5. Sair\033[0m")
    opcao = input("\033[94mEscolha uma opção: \033[0m")

    if opcao == "1":
        matricula = input("\033[96mDigite a matricula do aluno: \033[0m")
        nome = input("\033[93mDigite o nome do aluno completo: \033[0m")
        curso = input("\033[96mDigite o curso do aluno: \033[0m")
        AdicionarAluno(matricula, nome, curso)
    elif opcao == "2":
        matricula = input("\033[91mDigite a matrícula do aluno a ser removido: \033[0m")
        RemoverAluno(matricula) 
    elif opcao == "3":
        matricula = input("\033[92mDigite a matrícula do aluno a ser atualizado: \033[0m")
        nome = input("\033[93mDigite o novo nome do aluno: \033[0m")
        curso = input("\033[96mDigite o novo curso do aluno: \033[0m")
        AtualizarAluno(matricula, nome if nome else None, curso if curso else None)
    elif opcao == "4":
        ListarAlunos()
    elif opcao == "5":
        print("\033[1;31mDesligando...\033[0m")
        break        
    else:
        print("\033[91mOpção inválida. Tente novamente!\033[0m")

#Dei meu melhor ^^