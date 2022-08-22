qnt_alunos = int(input())
lista1 = []
lista2 = []
w = 0
for notas in range(qnt_alunos): #primeira nota
    nota = float(input())
    lista1.append(nota)
for bonus in range(qnt_alunos): #nota bônus
    nota_bonus = float(input())
    if lista1 [bonus] == 10:
        lista2.append(lista1[bonus])
    elif lista1 [bonus] == 9:
        lista2.append(lista1[bonus] + 1)
    elif nota_bonus == 10:
        lista2.append(lista1[bonus] + 2)
    else:
        lista2.append(lista1[bonus])
for a in range(qnt_alunos):
    if lista1 [a] != lista2 [a]:
        w = w+1
print (f'NOTAS ALTERADAS: {w}')
for c in range(qnt_alunos):
    if lista1 [c] == lista2 [c]:
        print (f'-({(c+1):0>3}) original: {lista1[c]:05.2f} | final: {lista1[c]:05.2f}')
    else:
        print (f'*({(c+1):0>3}) original: {lista1[c]:05.2f} | final: {lista2[c]:05.2f}')