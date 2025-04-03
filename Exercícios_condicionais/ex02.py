altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso(Kg): "))
imc = peso / altura ** 2
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 >= imc < 25:
    print("Você está saudável.")
elif 25 >= imc < 30:
    print("Você está acima do peso.")
elif imc > 30:
    print("Atenção! Você está obeso.")
