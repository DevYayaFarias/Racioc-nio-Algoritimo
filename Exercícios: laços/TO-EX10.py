def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes == 2:
        return 29 if eh_bissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    dias = 0
    
    while ano1 < ano2 or (ano1 == ano2 and mes1 < mes2) or (ano1 == ano2 and mes1 == mes2 and dia1 < dia2):
        dia1 += 1
        if dia1 > dias_no_mes(mes1, ano1):
            dia1 = 1
            mes1 += 1
            if mes1 > 12:
                mes1 = 1
                ano1 += 1
        dias += 1
    
    return dias

dia1, mes1, ano1 = map(int, input("Data inicial (DD MM AAAA): ").split())
dia2, mes2, ano2 = map(int, input("Data final (DD MM AAAA): ").split())

print(f"Dias entre as datas: {dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2)}")
