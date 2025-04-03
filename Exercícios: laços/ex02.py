maior = float('-inf')
menor = float('inf')
for i in range (5):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
       maior = num

print("O maior número é: ", maior)
print("O menor número é: ", menor)


