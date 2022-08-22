qnt_canais = int(input())
lista = []
for c in range(qnt_canais):
    canal = input().split(';')
    lista.append(canal)
x = float(input()) #premium
y = float(input()) #normal
print('-'*5)
print('BÔNUS')
print('-'*5)
for item in lista:
    print(f'{item[0]}: R$ ', end='')
    if item [3] == 'sim':
        print (f'{((float(item[1])//1000)*x)+float(item[2]):.2f}')
    elif item [3] == 'não':
        print (f'{((float(item[1])//1000)*y)+float(item[2]):.2f}')
