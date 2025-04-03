altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo (F\M): ").strip().upper()
peso_ideal = (72.7 * altura - 58) if sexo == "M" else (62.1 * altura - 44.7)
print(f"O seu peso ideal é: {peso_ideal}kg")

