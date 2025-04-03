print('1 – À vista em dinheiro ou cheque, recebe 10% de desconto')
print('2 – À vista no cartão de crédito, recebe 15% de desconto')
print("3 – Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10%")

preço = float(input("Insira o preço: R$"))
codigo = int(input("Qual a condição de pagamento? (1-4): "))
desconto = {1: 0.9, 2: 0.85, 3: 1, 4: 1.1}
total = preço * desconto.get(codigo, 0)
print(f"Total: R${total:.2f}")
