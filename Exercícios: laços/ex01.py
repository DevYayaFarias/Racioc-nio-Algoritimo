num_par = 0
num_ímpar = 0
resto = 0
for i in range (10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        num_par = num_par + 1
    else:
        num_ímpar = num_ímpar + 1

print("A quantidade de números pares é: ", num_par)
print("A quantidade de números ímpares é: ", num_ímpar)
''
