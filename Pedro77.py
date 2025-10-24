# Matriz de temperaturas [Cidades x Meses]
matriz = [
    [22, 25, 28, 32],  # Cidade 1
    [20, 23, 26, 30],  # Cidade 2
    [18, 22, 25, 29]   # Cidade 3
]

# Transpor a matriz (trocar linhas por colunas)
transposta = []
for i in range(len(matriz[0])):  # percorre as colunas
    linha = []
    for j in range(len(matriz)):  # percorre as linhas
        linha.append(matriz[j][i])
    transposta.append(linha)

# Mostrar matriz transposta
print("Matriz Transposta (Meses x Cidades):")
for linha in transposta:
    print(linha)
