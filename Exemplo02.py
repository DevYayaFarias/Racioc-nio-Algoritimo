n = int(input("Digite a quantidade de números: "))
for i in range(n):
    num = int(input(f"Digite o {i + 1}° número: "))
    if num %2 == 0:
       print("O valor informado é par!")
    else:
        print("O valor informado é ímpar!")
