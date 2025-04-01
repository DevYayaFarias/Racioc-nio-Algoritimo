num = int(input("Digite o número: "))
exp = int(input("Digite o expoente: "))
pot = 1
for _ in range(exp):
    pot *= num
print(num, "elevado a ", exp, "é igual a", pot)
