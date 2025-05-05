notas = []
for i in range(4):
 num = float(input(f"Digite {i+1}ª nota que tirou: "))
 notas.append(num)
media = sum(notas) / 4
print(f"As notas foram: {notas}")
print(f"A sua média é: {media}")
 
