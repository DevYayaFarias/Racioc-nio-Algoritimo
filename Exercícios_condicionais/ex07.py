meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
meses_completos = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
                   "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dia = int(input("Dia: "))
mes = int(input("Mês (1-12): "))
ano = int(input("Ano (com 4 dígitos): "))

opcao = int(input("Escolha o formato (1-Simples, 2-Abreviado, 3-Completo): "))

if opcao == 1:
    print(f"{dia:02d}/{mes:02d}/{ano}")
elif opcao == 2:
    print(f"{dia}/{meses[mes-1]}/{ano}")
elif opcao == 3:
    print(f"{dia} de {meses_completos[mes-1]} de {ano}")
else:
    print("Opção inválida!")
