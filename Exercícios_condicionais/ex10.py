def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    if int(cpf[9]) != (11 - soma % 11) % 10:
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    if int(cpf[10]) != (11 - soma % 11) % 10:
        return False

    return True

cpf = input("Digite o CPF (somente números): ")
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
