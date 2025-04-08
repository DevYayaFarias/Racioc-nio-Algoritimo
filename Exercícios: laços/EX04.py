"""
Conversão de número hexadecimal para decimal
C1x16^n-1 + C2x16^n-2 + .... + cn-1x16^1+cnx16^0
"""
hex = input("Digite um valor em hexadecimal: ")
dec = 0
exp = len(hex)
for c in hex:
  num = 0
  if c == "A":
    num = 10
  elif c == "B":
    num = 11
  elif c == "C":
    num = 12
  elif c == "D":
    num = 13
  elif c == "E":
    num = 14
  elif c == "F":
    num = 15
  else:
    num = int(c)
dec += num * 16 ** exp
exp -= 1

print(f"Valor em decimal:{dec}")
