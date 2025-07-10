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
linha = [0]*n
lower = []
for a in range(n):
    lower.append(linha)
for i in range(n):
    for j in range(i+1):
        soma = 0
        if i==j:
            for k in range(j):
                soma+= (lower[j][k]**2)
            lower[j][j] = int((matriz[j][j]-soma)**(1/2))
        else:
            for k in range(j):
                soma+= (lower[i][k]*lower[j][k])
            if lower[j][j]>0:
                lower[i][j]=(matriz[i][j]-soma)/lower[j][j]
    
    print('triangular inferior\t\ttransposta')
    
    for i in range(n):
        for j in range(n):
            print(lower[i][j], end='\t')
        print()
        for j in range(n):
            print(lower[j][i], end='\t')
        print()