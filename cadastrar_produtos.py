#Cadastrar Produtos
# 1. cadastrar_produto()
# 2. listar_estoque()
# 3. atualizar_quantidade()
# 4. remover_produto()
# 5. calcular_valor_total()
# 6. salvar_em_csv()
# 7. menu()

import csv

produtos = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    try:
        preco = float(input(f"Digite o preço do {nome}: R$"))
        produtos[nome] = {"preco": preco, "quantidade": 0}
        print(f"\nProduto {nome}, foi cadastrado com sucesso! \n")
    except ValueError:
        print("Preço inválido! Use ponto no lugar de vírgula")

def atualizar_quantidade():
    print("\n---Atualização da quantidade---")
    nome = input("Nome do produto para atualizar: ")
    if nome in produtos:
        try:
            nova_qtd = int(input("Digite a quantidade a adicionar: "))
            produtos[nome]["quantidade"] += nova_qtd
            print("Quantidade Atualizada!")
        except ValueError:
            print("Quantidade Inválida!")
    else:
        print("Produto não encontrado.")

def remover_produto():
    print("\n---Produto(s) Removido(s)")
    nome = input("Digite o produto a ser removido: ")
    if nome in produtos:
        confirmacao = input(f"Tem certeza que deseja remover '{nome}? [s/n]").lower()
        if confirmacao == "s":
            del produtos[nome]
            print(f"'{nome}' foi removido!")
        else:
            print("Remoção cancelada!")
    else:
        print(f"Produto '{nome}' não encontrado em estoque!")

def calcular_total():
    print("\n---Total do Estoque---")
    if not produtos:
        print("Estoque vazio.")
        return
    
    total = 0
    for item in produtos.values():
        total += item["preco"] * item["quantidade"]
    print(f"\nTotal do estoque: R${total:.2f}")

def lista_estoque():  #usar por ultimo
    print("\n---Produtos Disponiveis---")
    if not produtos:
        print("Estoque vazio.")
        return
    for nome, info in produtos.items():
        print(f"-{nome} -R${info['preco']:.2f} -Quantidade: {info['quantidade']}")

def salvar_csv():
    print("\nSalvar Estoque")
    if not produtos:
        print("Estoque Vazio")
        return
    
    with open("estoque.csv", mode="w", newline="", encoding="utf-8")as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Produto", "Preço (R$)", "Quantidade"])
        for nome, info in produtos.items():
            escritor.writerow([nome, f"{info['preco']:.2f}", info['quantidade']])
        print("Estoque salvo com sucesso em 'estoque.csv'!")

def pesquisar_produtos():
    print("\n---Pesquisar Produtos---")
    nome = input("Digite o nome do produto a pesquisar: ").strip().lower()
    if nome in produtos:
        info = produtos[nome]
        print("\nProduto Encontrado")
        print(f"Nome: {nome}")
        print(f"Preço: R${info['preco']:.2f}")
        print(f"Quantidade: {info['quantidade']}")
    else:
        print(f"\nProduto '{nome} não escontradp")

while True:
    print("\n==Menu==")
    print("1. Cadastrar Produto")
    print("2. Atualizar Produto")
    print("3. Remover Produto")
    print("4. Calcular Valor Total")
    print("5. Listar Estoque")
    print("6. Pesquisar Produto(s)")
    print("7. Salvar Estoque em CSV")
    print("8. Sair")

    opcao = input("Escolha a Opção: ").strip()

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        atualizar_quantidade()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        calcular_total()
    elif opcao == "5":
        lista_estoque()
    elif opcao == "6":
        pesquisar_produtos()
    elif opcao == "7":
        salvar_csv()
    elif opcao == "8":
        print("Saindo!")
        break
    else:
        print("Opção inválida!")


        

