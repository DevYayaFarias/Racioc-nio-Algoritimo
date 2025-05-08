print("-- BEM-VINDO AO RESTAURANTE BOCA FELIZ!! --")

estoque = {
    'pao': 10,
    'hamburguer': 12,
    'tomate': 5,
    'bacon': 5,
    'ovo': 5
}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}


while True:
    print("\n*-*-*- CARDÁPIO BOCA FELIZ -*-*-*")
    for item in cardapio:
        print(f"- {item}")
    pedido = input("O que deseja pedir (0 para sair)? ").strip().lower()

    if pedido == "0":
        print("Encerrando pedidos. Até a próxima!")
        break

    if pedido not in cardapio:
        print("Item não localizado no cardápio")
        continue

    ingredientes_necessarios = cardapio[pedido]
    faltando = []

    for ingrediente in ingredientes_necessarios:
        if ingrediente not in estoque or estoque[ingrediente] < ingredientes_necessarios.count(ingrediente):
            if ingrediente not in faltando:
                faltando.append(ingrediente)

    if faltando:
        for ingrediente in faltando:
            print(f"Que pena. Infelizmente acabou o {ingrediente}")
        continue

    for ingrediente in ingredientes_necessarios:
        estoque[ingrediente] -= 1

    print(f"Um {pedido} saindo no capricho!!!")
