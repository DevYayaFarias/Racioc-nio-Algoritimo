import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Não há raízes reais."
    
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return x1, x2

a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))

if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    resultado = calcular_raizes(a, b, c)
    print(f"Raízes: {resultado}")
