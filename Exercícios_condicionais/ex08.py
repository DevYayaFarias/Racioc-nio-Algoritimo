import datetime

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

unidade = input("O que você quer acrescentar? (segundo, minuto, hora, dia, mes, ano): ")
incremento = int(input(f"Quantos {unidade}s você quer adicionar? "))

data = datetime.datetime(ano, mes, dia, hora, minuto, segundo)

if unidade == "segundo":
    nova_data = data + datetime.timedelta(seconds=incremento)
elif unidade == "minuto":
    nova_data = data + datetime.timedelta(minutes=incremento)
elif unidade == "hora":
    nova_data = data + datetime.timedelta(hours=incremento)
elif unidade == "dia":
    nova_data = data + datetime.timedelta(days=incremento)
elif unidade == "mes":
    nova_data = data.replace(month=data.month + incremento)
elif unidade == "ano":
    nova_data = data.replace(year=data.year + incremento)


print(f"Nova data e hora: {nova_data}")



