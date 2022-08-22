tempo = 0
contador = 0
soma = 0
lista = []
while tempo >= 0:
    tempo = int(input())
    if tempo > 0:
        lista.append(tempo)
        soma = soma + tempo
        contador = contador + 1
    else: 
        break

media = soma/contador
print (f'MEDIA: {media:.2f}')
for numero in lista:
    if numero < media:
        print(numero)
    else:
        continue