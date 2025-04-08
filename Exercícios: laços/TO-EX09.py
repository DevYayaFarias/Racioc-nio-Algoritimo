decimal = int(input("Digite um número decimal: "))
hex_chars = "0123456789ABCDEF"
hexadecimal = ""

while decimal > 0:
    resto = decimal % 16
    hexadecimal = hex_chars[resto] + hexadecimal
    decimal = decimal // 16

print(f"Hexadecimal: {hexadecimal if hexadecimal else '0'}")
