import math
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
linha = [0]*n
g = [[0]*n]*n
for k in range(n):
    s = 0
    for j in range(k):
        s = s + g[k][j]**2
    r = matriz[k][k] - s
    g[k][k] = math.sqrt(r)
    for i in range(k+1, n):
        s = 0
        for j in range(1, k-1):
            s = s + g[i][j]*g[k][j]
        g[i][k] = (matriz[i][k] - s)/g[k][k]
print(g,'\t')