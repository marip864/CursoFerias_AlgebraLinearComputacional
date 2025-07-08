matriz = []
vetor = []

# Entrada da ordem da matriz
n = int(input('Digite a ordem (n) da matriz A: '))

# Entrada da matriz A
for i in range(n):
    linha = list(map(int, input(f'Digite os {n} coeficientes da linha {i+1}: ').split()))
    if len(linha) != n:
        print("Número incorreto de coeficientes. Tente novamente.")
        exit()
    matriz.append(linha)

# Entrada do vetor B
vetor = list(map(int, input(f'Digite os {n} elementos do vetor B: ').split()))
if len(vetor) != n:
    print("Número incorreto de elementos no vetor. Tente novamente.")
    exit()

# Vetor solução
x = [0] * n

# Eliminação de Gauss com pivotamento parcial
for k in range(n - 1):
    # Escolha do pivô
    pivo = abs(matriz[k][k])
    indice_pivo = k
    for i in range(k + 1, n):
        if abs(matriz[i][k]) > pivo:
            pivo = abs(matriz[i][k])
            indice_pivo = i

    if pivo == 0:
        print("Sistema sem solução única.")
        exit()

    # Troca de linhas se necessário
    if indice_pivo != k:
        matriz[k], matriz[indice_pivo] = matriz[indice_pivo], matriz[k]
        vetor[k], vetor[indice_pivo] = vetor[indice_pivo], vetor[k]

    # Eliminação
    for i in range(k + 1, n):
        m = matriz[i][k] / matriz[k][k]
        vetor[i] -= m * vetor[k]
        for j in range(k, n):
            matriz[i][j] -= m * matriz[k][j]

# Substituição para trás
x[n - 1] = vetor[n - 1] / matriz[n - 1][n - 1]
for k in range(n - 2, -1, -1):
    s = sum(matriz[k][j] * x[j] for j in range(k + 1, n))
    x[k] = (vetor[k] - s) / matriz[k][k]

# Impressão da solução
for i in range(n):
    print(f"x[{i}] = {x[i]:.4f}")

