from string import digits


def retira_formatacao(num_cpf):   
    cpf = ''.join(num for num in num_cpf if num in digits)
    return cpf


def valida_cpf(num_cpf):
    cpf = [int(digits) for digits in num_cpf if digits.isdigit()]
        
    for digits in cpf:        
        if cpf.count(0) > 10: return "CPF INVALIDO"
        if cpf.count(1) > 10: return "CPF INVALIDO"
        if cpf.count(2) > 10: return "CPF INVALIDO"
        if cpf.count(3) > 10: return "CPF INVALIDO"
        if cpf.count(4) > 10: return "CPF INVALIDO"
        if cpf.count(5) > 10: return "CPF INVALIDO"
        if cpf.count(6) > 10: return "CPF INVALIDO"
        if cpf.count(7) > 10: return "CPF INVALIDO"
        if cpf.count(8) > 10: return "CPF INVALIDO"
        if cpf.count(9) > 10: return "CPF INVALIDO"

    if len(cpf) != 11:
        return "CPF INVALIDO"

    soma_primeiro = sum(x*y for x, y in zip(cpf[0:9], range(10, 1, -1)))
    divisao_dez = (soma_primeiro * 10 % 11) % 10
    
    soma_segundo = sum(x*y for x, y in zip(cpf[0:10], range(11, 1, -1)))
    divisao_onze = (soma_segundo * 10 % 11) % 10

    if cpf[9] != divisao_dez:
        return "CPF INVALIDO"
    if cpf[10] != divisao_onze:
        return "CPF INVALIDO"

    return "CPF VALIDO"



