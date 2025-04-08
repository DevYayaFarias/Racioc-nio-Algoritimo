numeros = []
for _ in range(5):
    num = float(input("Digite um número: "))
    numeros.append(num)


for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Números ordenados:", numeros)
