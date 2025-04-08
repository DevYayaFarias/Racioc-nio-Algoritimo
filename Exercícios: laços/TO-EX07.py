cont = 0
while True:
    palavra = input("Digite uma palavra (vazio para parar): ").lower()
    if palavra == "":
        break
    cont += palavra.count('a')

print(f"Total de letras 'A': {cont}")
