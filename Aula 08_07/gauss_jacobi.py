matriz = []
elementoInt = []
vetorInt = []
vetorSolucao = []
vetorSolucaoInt = []
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
vetorSolucao = input('Digite o vetor solução:').split()
for v in vetorSolucao:
    v = int(v)
    vetorSolucaoInt.append(v)
vetorSolucao = vetorSolucaoInt
iteracoes = int(input('Agora, digite o número de interações que quer realizar:'))
while iteracoes!=0:
    iteracao = 0
    vetorAuxiliar = [0]*n
    while iteracao<iteracoes:
        for i in range(len(matriz)):
            x = vetor[i]
            for j in range(len(matriz)):
                if i!=j:
                    x-=matriz[i][j]*vetorSolucao[j]
            vetorAuxiliar[i] = x/matriz[i][i]
        iteracao+=1

        for p in range(len(vetorAuxiliar)):
            vetorSolucao[p] = vetorAuxiliar[p]
    print(vetorSolucao)
    iteracoes = int(input('Agora, digite o número de interações que quer realizar:'))