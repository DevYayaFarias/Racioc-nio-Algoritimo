preco = {
    "Norte": (500, 900),
    "Nordeste": (350, 650),
    "Centro-Oeste": (350, 600),
    "Sul": (300, 550)
}

print("Destinos disponíveis: 1- Norte, 2- Nordeste, 3- Centro-Oeste ou 4- Sul")
destino = input("Informe seu destino: ").strip().title()

if destino in preco:
    ida_volta = input("Ida e volta? (s/n): ").strip().lower() == "s"
    valor = preco[destino][1 if ida_volta else 0]
    print(f"Preço: R$ {valor:.2f}")
else:
    print("Destino inválido!")
