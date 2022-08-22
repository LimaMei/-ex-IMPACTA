s=[48,5,39,56,40,52]

def troca(s,i,j):
    s[i], s[j] =s[j] ,s[i]


def empurra_minimo(s, n):
    for i in range (n-1):
        if s[i] < s[i+1]:
            troca(s, i, i+1)


def empurra_maximo (s,n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)


def bubble_sort(s, crescente=False):
    n = len(s)
    if crescente:
        empurra=empurra_maximo
    else:
        empurra=empurra_minimo
    while n>1:
        empurra(s, n)
        n -=1

bubble_sort (s)
print(s)