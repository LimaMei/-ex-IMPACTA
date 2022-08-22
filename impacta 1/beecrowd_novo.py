def somatemp():
    soma = 0
    cont = 1
    while (cont <= 30):
        temp = float(input())
        soma = soma + temp
        cont = cont + 1
    return soma


S = somatemp()
print('A soma das temperaturas é ', S)
