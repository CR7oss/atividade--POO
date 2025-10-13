# Estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender(estoque, produto, quantidade):
    if estoque[produto - 1] >= quantidade:
        estoque[produto - 1] -= quantidade
        print(f"Venda realizada: Produto {produto}, {quantidade} unidades vendidas.")
    else:
        print(f"Estoque insuficiente para o produto {produto}!")

# Função para adicionar produtos
def adicionar(estoque, produto, quantidade):
    estoque[produto - 1] += quantidade
    print(f"Foram adicionadas {quantidade} unidades ao produto {produto}.")

# Função para exibir o estoque
def exibir(estoque):
    print("\nEstoque atual:")
    for i in range(len(estoque)):
        print(f"Produto {i+1}: {estoque[i]} unidades")

# ---- Procedimento experimental ----

# Atualiza o estoque conforme as vendas
vender(estoque, 1, 3)
vender(estoque, 4, 2)

# Adiciona novas unidades ao produto 5
adicionar(estoque, 5, 10)

# Exibe o estoque final
exibir(estoque)