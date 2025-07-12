#aula teste

alunos = []

def calcular_media(p1, p2, trabalho):
    media = (p1 *4 + p2*4 + trabalho*2)/10
    return media

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def add_aluno (nome, matricula, p1, p2, trabalho):
    media = calcular_media(p1, p2, trabalho)
    situacao = definir_situacao(media)
    aluno = {
        "nome" : nome, 
        "matricula" : matricula,
        "notas" : [p1, p2, trabalho],
        "media": media,
        "situacao": situacao
    }
    alunos.append(aluno)

while True:
    print("\n---Cadastro de Alunos---")
    nome = input(f"n\Digite o nome do aluno (ou sair para encerrar): ")
    if nome.lower() == "sair":
        break

    matricula = input("Digite a matricula: ")

    while True: 
        try:
            p1 = float(input("digite sua nota da p1: "))
            p2 = float(input("digite sua nota da p2: "))
            trabalho = (float(input("digite sua nota do trabalho: ")))
            break
        except ValueError:
            print("Entrada inválida, tente ponto ao invés de vírgula!")

    add_aluno(nome, matricula, p1, p2, trabalho)

print("n\---Boletim---")
for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Matricula: {aluno['matricula']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média final: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")





    


