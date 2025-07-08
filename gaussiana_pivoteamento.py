
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
vetor = input('Digite o vetor B:').split()
for e in vetor:
    e = int(e)
    vetorInt.append(e)
vetor = vetorInt
for k in range(1, n-1):
    pivo = abs(matriz[k][k])
    indice_pivo = k
    for i in range(k+1, n):
        if abs(matriz[i][k])>pivo:
            pivo = abs(matriz[i][k])
            indice_pivo = i
    if pivo==0:
        exit()
    if indice_pivo!=k:
        for j in range(1, n):
            troca = matriz[k][j]
            matriz[k][j] = matriz[indice_pivo][j]
            matriz[indice_pivo][j] = troca
        troca = vetor[k]
        vetor[k] = vetor[indice_pivo]
        vetor[indice_pivo] = troca

    for i in range(k+1, n):
        m = matriz[i][k]/matriz[k][k]
        vetor[i] = vetor[i]-(m*vetor[k])
        for j in range(k+1, n):
            matriz[i][j] = matriz[i][j]-(m*matriz[k][j])
    x[n-1] = vetor[n-1]/matriz[n-1][n-1]
    for k in range(n-1, 1):
        s = 0
        for j in range(k+1, n):
            s = s+matriz[k][j]*x[j]
            x[k] = (vetor[k]-s)/matriz[k][k]
for i in range(n):
    print(f"x[{i}] = {x[i]}")


