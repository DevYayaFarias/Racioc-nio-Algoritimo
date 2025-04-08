cont = 0
while True:
    palavra = input("Digite uma palavra (vazio para parar): ").lower()
    if palavra == "":
        break
    cont += palavra.count('a')

print(f"Total de letras 'A': {cont}")


#OUTRA OPÇÃO, VISTO EM SALA:
cont = 0
while True:
    palavra = input("Digite uma palavra (<enter> para parar): ").lower()
    if palavra == "":
        break
    for l in palavra:
        if l == "a" or l =="A":
        cont += 1

print(f"Total de letras 'A': {cont}")
