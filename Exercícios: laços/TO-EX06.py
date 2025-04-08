nome = input("Digite seu nome completo: ").split()
print(f"Primeiro nome: {nome[0]}, Último nome: {nome[-1]}")

#Outra opção vista em sala de aula:
name = input("Digite seu nome completo: ")
first = ""
last = ""
for l in name:
  if l == " ":
    break
  first +=l
inv = ""
for l in name:
  inv = l + inv
for l in inv:
  if l == " ":
    break
  last = l + last
print(f"Primeiro nome: {first}\nSegundo nome: {last}")
