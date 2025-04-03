vogais = "aeiou"
consoante = ""
text = input("Digite o texto: ")
for l in text:
    if l in "bcdfghjklmnpqrstvwxyz":
        consoante += l
print("text", consoante)
