print("Que comecem os jogos!! Dois jogadores devem dar seu palpite (par ou ímpar) e escolher valores de 1 a 5. Quem acertar vence.")

Jogador1 = input("Jogador 1, escolha par ou ímpar: ").strip().lower()
while Jogador1 not in ["par", "ímpar"]:
    print("Escolha inválida! Digite 'par' ou 'ímpar'.")
    Jogador1 = input("Jogador 1, escolha par ou ímpar: ").strip().lower()
      
Jogador2 = "ímpar" if Jogador1 == "par" else "par"
print(f"Jogador 2, seu palpite é automaticamente '{Jogador2}'.")

num1 = int(input("Jogador 1, digite um valor (1 a 5): "))
while num1 < 1 or num1 > 5:
    print("Número inválido! Escolha um número entre 1 e 5.")
    num1 = int(input("Jogador 1, digite um valor (1 a 5): "))

num2 = int(input("Jogador 2, digite um valor (1 a 5): "))
while num2 < 1 or num2 > 5:
    print("Número inválido! Escolha um número entre 1 e 5.")
    num2 = int(input("Jogador 2, digite um valor (1 a 5): "))

soma = num1 + num2
resultado = "par" if soma % 2 == 0 else "ímpar"

if resultado == Jogador1:
    print(f"Jogador 1 venceu!! A soma foi {soma}, que é {resultado}.")
else:
    print(f"Jogador 2 venceu!! A soma foi {soma}, que é {resultado}.")
