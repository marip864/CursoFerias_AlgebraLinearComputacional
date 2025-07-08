matriz = []
elementoInt = []
vetorInt = []
n = int(input('Digite a ordem (n) da matriz A:'))
x = [0]*n
for i in range(n):
    elemento = input('Digite os coeficientes da linha:')
    elemento = elemento.split()
    for e in elemento:
        e = int(e)
        elementoInt.append(e)
    matriz.append(elementoInt)
    elementoInt = []
print(matriz)


# Inicialização de L e U
L = [[0 for _ in range(n)] for _ in range(n)]
U = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    # Matriz U
    for k in range(i, n):
        U[i][k] = matriz[i][k] - sum(L[i][j] * U[j][k] for j in range(i))

    # Matriz L
    L[i][i] = 1
    for k in range(i+1, n):
        L[k][i] = (matriz[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]

print("Matriz L:")
for linha in L:
    print(linha)

print("\nMatriz U:")
for linha in U:
    print(linha)

# Entrada do vetor B
vetor = list(map(int, input(f'Digite agora os {n} elementos do vetor B: ').split()))
if len(vetor) != n:
    print("Número incorreto de elementos no vetor. Tente novamente.")
    exit()

y = [0]*n
