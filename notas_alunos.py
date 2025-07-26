import csv
import os

alunos = {}

def calcular_media(p1, p2, trabalho):
    return (p1*4 + p2*4 + trabalho*2)/10

def situacao_aluno(media):
    if media >= 7:
        return "Aprovado!"
    elif media >= 5:
        return"Recuperação!"
    else:
        return "Reprovado!"
    

def cadastrar_alunos():
    print("---Cadastro de Alunos---")
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if nome.replace(" ", "").isalpha():
            break
        else:
            print("Digite apenas letras!")
    while True:        
        try:
            p1 = float(input("Digite a nota da P1:"))
            p2 = float(input("Digite a nota da P2:"))
            trabalho = float(input("Digite a nota do Trabalho:"))
            break
        except ValueError:
            print("Erro: use ponto no lugar de vírgula ou digite apenas números!")
            
    media = calcular_media(p1, p2, trabalho)
    situacao = situacao_aluno(media)
    alunos[nome]= {
        "notas": {"P1": p1, "P2": p2, "Trabalho": trabalho},
        "media": round(media, 2),
        "situacao": situacao
    }
        
    print(f"\n{nome} cadastrado com sucesso.")

def atualizar_aluno(): 
    print("\n---Atualizar informações de Alunos---")
    nome = input("\nDigite o nome do aluno que deseja atualizar: ").strip()
    if nome in alunos:
        while True:
            try:
                p1 = float(input("Nova nota da P1:"))
                p2 = float(input("Nova nota da P2:"))
                trabalho = float(input("Nova nota do Trabalho:"))
                break
            except ValueError:
                print("Erro: use ponto no lugar de vírgula, ou digite apenas números!")
                
        media = calcular_media(p1, p2, trabalho)
        situacao = situacao_aluno(media)
        alunos[nome]["notas"] = {"P1": p1, "P2": p2, "Trabalho": trabalho}
        alunos[nome]["media"] = round(media, 2)
        alunos[nome]["situacao"] = situacao
        print(f"Notas de {nome} atualizadas com sucesso!")
    else:
        print("Aluno não encontrado.")
    
def remover_aluno():
    print("\n---Remover Aluno---")
    nome = input("\nDigite o nome do aluno que deseja remover: ").strip()
    if nome in alunos:
        confirmar = input(f"Tem certeza que deseja remover {nome}? (s/n): ").lower()
        if confirmar == "s":
            del alunos[nome]
            print(f"'{nome} foi removido!")
        else:
            print("Remoção Cancelada.")
    else:
        print(f"'{nome}' não encontrado")

def listar_aluno():
    print("\n---Boletim---")
    if not alunos:
        print("Aluno não cadastrado!")
        return
    for nome, dados in alunos.items():
        print(f"\nNome: {nome}")
        for tipo, nota in dados['notas'].items():
            print(f"{tipo}: {nota:.2f}")
        print(f"Média: {dados['media']:.2f}")
        print(f"Situação: {dados['situacao']}")
       
def salvar_csv():
    print("\n---Salvar Dados---")
    if not alunos:
        print("Aluno não encontrado")
        return
    
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "P1", "P2", "Trabalho", "Média", "Situação"])
        for nome, dados in alunos.items():
            escritor.writerow([
                nome,
                dados['notas']['P1'],
                dados['notas']['P2'],
                dados['notas']["Trabalho"],
                dados['media'],
                dados['situacao']
            ])

    print("Dados do aluno salvo com sucesso em 'alunos.csv'")

def carregar_dados_csv():
    if not os.path.exists("alunos.csv"):
        return
    
    with open("alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            nome = linha["Nome"]
            alunos[nome] = {
                "notas": {
                    "P1": float(linha["P1"]),
                    "P2": float(linha["P2"]),
                    "Trabalho": float(linha["Trabalho"]),
                },
                "media": float(linha["Média"]),
                "situacao": linha["Situação"]
            }

while True:
    print("\n===Menu===")
    print("1. Cadastrar Alunos")
    print("2. Atualizar Aluno")
    print("3. Remover Aluno")
    print("4. Listar Boletim")
    print("5. Salvar CSV")
    print("6. Carregar CSV")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_alunos()
    elif opcao == "2":
        atualizar_aluno()
    elif opcao == "3":
        remover_aluno()
    elif opcao == "4":
        listar_aluno()
    elif opcao == "5":
        salvar_csv()
    elif opcao == "6":
        carregar_dados_csv()
    elif opcao == "7":
        print("Até logo.")
        break

    else:
        print("Opção Inválida!")





    


