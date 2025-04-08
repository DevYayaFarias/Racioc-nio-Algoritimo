massa = float(input("Digite a massa inicial (em gramas): "))
tempo = 0

while massa >= 0.5:
    massa /= 2
    tempo += 50

print(f"Massa final: {massa} gramas")
print(f"Tempo necessário: {tempo} segundos")
