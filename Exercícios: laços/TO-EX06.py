nome = input("Digite seu nome completo: ").split()
print(f"Primeiro nome: {nome[0]}, Último nome: {nome[-1]}")

#Outra opção vista em sala de aula:
name = input("Digite seu nome completo: ")
first = ""
for l in name:
  if l == " ":
    break
  first +=l
print(first)
