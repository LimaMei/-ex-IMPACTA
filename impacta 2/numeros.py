# Programação Orientada a Objetos
# AC01 POO-EaD - Números especiais
#
# Email Impacta: gabriel.lsilva@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    if n < 2:
        return False
    qtd_divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            qtd_divisores += 1
        i += 1
    if qtd_divisores == 2:
        return True
    else:
        return False


def lista_primos(n):
    lista = []
    for i in range(2, n):
        if eh_primo(i):
            lista.append(i)
    return lista


def conta_primos(s):
    d = {}
    for item in s:
        if eh_primo(item):
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
    return d


def eh_armstrong(n):
    if n >= 0:
        n_string = str(n)
        tam = len(n_string)
        soma = 0
        for item in n_string:
            soma += int(item)**tam
        if soma == n:
            return True
        else:
            return False


def eh_quase_armstrong(n):
    if n >= 0:
        n_string = str(n)
        tam = len(n_string)
        soma = 0
        for item in n_string:
            soma += int(item)**tam
        if soma == n + 1 or soma == n - 1:
            return True
        else:
            return False


def lista_armstrong(n):
    lista = []
    for item in range(n):
        if eh_armstrong(item):
            lista.append(item)
    return lista


def eh_perfeito(n):
    if n >= 2:
        divisores = []
        for item in range(1, n):
            if n % item == 0:
                divisores.append(item)
    else:
        return False
    return sum(divisores) == n


def lista_perfeitos(n):
    if n >= 2:
        lista = []
        for item in range(2, n):
            if eh_perfeito(item):
                lista.append(item)
        return lista
