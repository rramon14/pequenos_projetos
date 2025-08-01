# Gerenciador de Tarefas

tarefas = []

def adicionar_tarefas():
    print("---Adicionar Tarefas---")
    tarefa = input("Digite a tarefa: ").strip()

    while True:
        prioridade = input("Digite a prioridade (baixa/média/alta): ").strip().lower()
        if prioridade in ['baixa', 'media', 'média', 'alta']:
            if prioridade == 'media':
                prioridade = 'média'
            break
        else:
            print("Prioridade inválida. Use: baixa, média ou alta.")

    nova_tarefa = {
        "tarefa": tarefa,
        "prioridade": prioridade,
        "status": "pendente"
    }

    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\n---Listar Tarefas---")
    if not tarefas:
        print("Tarefas não adicionada!")
        return
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. Tarefa: {tarefa['tarefa']}")
        print(f"   Prioridade: {tarefa['prioridade'].capitalize()}")
        print(f"   Status: {tarefa['status'].capitalize()}\n")

def tarefa_concluida():
    print("\n---Status da Tarefa---")
    if not tarefas:
        print("Nenhuma tarefa para concluir.")
        return
    
    for i, tarefa in enumerate(tarefas, 1):
        status = tarefa["status"]
        print(f"{i}. {tarefa['tarefa']} - Status: {status}")

    try:
        escolha = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]['status'] = 'concluída'
            print(f"Tarefa '{tarefas[escolha - 1]['tarefa']}' marcada como concluída.")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido")

def remover_tarefa():
    print("\n---Remover Tarefa(s)---")
    if not tarefas:
        print("Tarefa não encontrada")
        return
    
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']} - Status: {tarefa['status']} ")

    try:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <=len(tarefas):
            confirmacao = input(f"Tem certeza que deseja remover {tarefas[indice - 1]['tarefa']}? (s/n)").lower()
            if confirmacao == "s":
                removida = tarefas.pop(indice -1)
                print(f"Tarefa '{removida['tarefa']}' foi removida com sucesso!")
            else:
                print("Remoção cancelada!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")
              
def filtrar_tarefas():
    print("\n---Prioridades da(s) Tarefa(s)---")
    if not tarefas:
        print("Tarefa não encontrada!")
        return
    
    prioridade_filtro = input("Digite a prioridade para filtrar (baixa/média/alta): ").strip().lower()

    if prioridade_filtro == "media":
        prioridade_filtro = "média"

    if prioridade_filtro not in ["baixa", "média", "alta"]:
        print("Prioridade inválida! Use: baixa, média, alta.")

    filtradas = [t for t in tarefas if t ["prioridade"] == prioridade_filtro]

    if not filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade_filtro}'.")
    else:
        print(f"\nTarefas com prioridade '{prioridade_filtro}': ")
        for i, tarefa in enumerate(filtradas, 1):
            print(f"{i}. {tarefa['tarefa']} - Status: {tarefa['status']}") 

while True:
    print("\n===Menu===")
    print("1. Adicionar Tarefa(s)")
    print("2. Listar Tarefa(s)")
    print("3. Tarefa(s) Concluída(s)")
    print("4. Remover Tarefa(s)")
    print("5. Filtrar Tarefa(s)")
    print("6. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_tarefas()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        tarefa_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        filtrar_tarefas()
    elif opcao == "6":
        print("Sair")
        break
    else:
        print("Opção inválida!")










