vetores = []
for i in range(10):
  num = i+1
  num = float(input("Digite o número: "))
  vetores.append(num)
for i in reversed(range(10)):
    print("Números na ordem inversa: ",vetores[i])
