lista1 = input().split()
lista2 = []
for c in lista1:
    lista2.append(int(c))
lista2.sort()
comando, codigo = input().split()
codigo = int(codigo)
while True:
    if comando == 'exibir':
        lista2.sort()
        print(lista2)
    elif comando == 'adicionar':
        lista2.append(codigo)
    elif comando == 'remover':
        lista2.remove(codigo)
    elif comando == 'encerrar':
        lista2.sort()
        print(lista2)