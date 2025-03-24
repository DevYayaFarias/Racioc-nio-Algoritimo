
# 1. Elaborar um algoritmo que solicita dois números ao usuário e exibe a soma destes números.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"A soma é: {num1 + num2}")




# 2. Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula sua idade com
# relação ao ano de 2020, sendo que o usuário já fez aniversário neste ano.

ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2020 - ano_nascimento
print(f"Você tem {idade} anos em 2020.")




# 3. Criar um programa que solicita um número ao usuário, e informa se este número é 
# par ou ímpar. Dica: para saber se um número é par ou ímpar calcule o resto da divisão
# deste número por 2 (operador %). Se o resultado for 0 o número é par, 1 é ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")




# 4. Criar um programa que solicita ao usuário o seu salário. Se o valor for inferior a 5000
# calcule um abono de final de ano de 15%. Caso contrário, o abono será de 10%. 
# Informe ao usuário seu valor de abono de final de ano.

salario = float(input("Digite seu salário: "))
if salario < 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.10
print(f"Seu abono de final de ano será: R$ {abono:.2f}")




# 5. Criar um programa que pergunte ao usuário em que turno trabalha. Formato da entrada:
# M - Manhã ou T - Tarde ou N - Noite. Mostre a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

turno = input("Digite seu turno de trabalho (M - Manhã, T - Tarde, N - Noite): ").strip().upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "T":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")




# 6. Criar um programa que solicite ao usuário dois números e a operação que deseja executar
# entre eles. Mostrar o resultado desta operação no formato: num1 op num2 = resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None
if resultado is not None:
    print(f"{num1} {operacao} {num2} = {resultado}")




# 7. Criar um programa que pergunta o tamanho de três lados de um triângulo, e informa que 
# tipo de triângulo que é, a saber: 
# a. Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado;
# b. Equilátero: triângulo que tem todos os lados iguais;
#c. Isóceles: triângulo que tem dois lados iguais;
#d. Escaleno: triângulo que tem todos os lado diferentes

a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")





# 8. Criar um programa que solicitado ao usuário as quatro notas bimestrais de um matéria e
# quantas faltas este aluno teve. Informar se o aluno foi aprovado ou reprovado, bem como o motivo. A saber:
#a. A média anual é 7;
#b. A disciplina possui 40 aulas;
#c. O mínimo exigido é 75% de presença.

notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(4)]
faltas = int(input("Digite o número de faltas: "))
media = sum(notas) / 4
presenca = ((40 - faltas) / 40) * 100
if media >= 7 and presenca >= 75:
    print("Aluno Aprovado!")
elif media < 7:
    print("Aluno Reprovado por nota!")
else:
    print("Aluno Reprovado por falta!")




# 9. Criar um Programa que simule um caixa eletrônico. O programa deverá perguntar ao
#usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. A saber:
#a. Notas disponíveis: 1, 5, 10, 50 e 100 reais;
#b. Valor mínimo de saque: R$ 10,00 reais;
#c. Valor máximo de saque: R$ 600,00 reais

valor = int(input("Digite o valor do saque (entre 10 e 600): "))
if valor < 10 or valor > 600:
    print("Valor inválido!")
else:
    notas = [100, 50, 10, 5, 1]
    distribuicao = {}
    for nota in notas:
        distribuicao[nota], valor = divmod(valor, nota)
    print("Notas fornecidas:")
    for nota, qtd in distribuicao.items():
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ {nota}")



# 10. Calcular IRPF:

rendimento = float(input("Digite seu rendimento mensal: "))
num_dependentes = int(input("Digite o número de dependentes: "))
pensao = float(input("Digite o valor da pensão alimentícia: "))
outras_deducoes = float(input("Digite o valor de outras deduções: "))

deducao_dependente = 189.59 * num_dependentes
base_calculo = rendimento - (deducao_dependente + pensao + outras_deducoes)

if base_calculo <= 1903.98:
    aliquota = 0.0
    imposto = 0.0
elif base_calculo <= 2826.65:
    aliquota = 0.075
    imposto = (base_calculo - 1903.98) * aliquota
elif base_calculo <= 3751.05:
    aliquota = 0.15
    imposto = (base_calculo - 2826.65) * aliquota + (2826.65 - 1903.98) * 0.075
elif base_calculo <= 4664.68:
    aliquota = 0.225
    imposto = (base_calculo - 3751.05) * aliquota + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075
else:
    aliquota = 0.275
    imposto = (base_calculo - 4664.68) * aliquota + (4664.68 - 3751.05) * 0.225 + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075

aliquota_efetiva = (imposto / base_calculo) * 100 if base_calculo > 0 else 0

print(f"Imposto a pagar: R$ {imposto:.2f}")
print(f"Faixa de rendimento: {aliquota * 100:.1f}%")
print(f"Taxa efetiva aplicada: {aliquota_efetiva:.2f}%")

