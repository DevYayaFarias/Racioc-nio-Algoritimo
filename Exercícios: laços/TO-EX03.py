pontos_vencedor = int(input("Pontos para vencer: "))
pontos_jogador1 = 0
pontos_jogador2 = 0

while pontos_jogador1 < pontos_vencedor and pontos_jogador2 < pontos_vencedor:
    jogador1 = input("Jogador 1: ").lower()
    jogador2 = input("Jogador 2: ").lower()

    if jogador1 == jogador2:
        print("Empate!")
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "papel" and jogador2 == "pedra") or \
         (jogador1 == "tesoura" and jogador2 == "papel"):
        pontos_jogador1 += 1
        print("Jogador 1 venceu a rodada!")
    else:
        pontos_jogador2 += 1
        print("Jogador 2 venceu a rodada!")

if pontos_jogador1 > pontos_jogador2:
    print("Jogador 1 venceu o jogo!")
else:
    print("Jogador 2 venceu o jogo!")
