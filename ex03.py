print("Que comecem os jogos!! Dois jogares devem dar seu palpite (par ou ímpar) de valores de 1 a 5. Quem acertar vence.")
Jogador1 = input("Jogador 1 dê deu palpite (par/ímpar): ").strip().lower()
num1 = int(input("Jogador 1 Digite um valor (1 a 5): "))
Jogador2 = input("Jogador 2 dê deu palpite (par/ímpar): ").strip().lower()
num2 = int(input("Jogador 2 Digite um valor (1 a 5): "))

if 1 <= num1 <= num2 and 1 <= num2 <= 5 and Jogador1 != Jogador2:
    resultado = "par" if (num1 + num2) % 2 == 0 else "ímpar"
    vencedor = "Jogador 1" if (num1 + num2) % 2 == (Jogador1 == "par") else "Jogador 2"
    print(f"{vencedor} venceu!!");
else:
    print("rodada inválida")