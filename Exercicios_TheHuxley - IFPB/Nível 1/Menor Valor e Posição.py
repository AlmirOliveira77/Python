lista = []
l = []

num = int(input())
valor = input().split(" ")
lista.append(valor)

for i in lista:
    for j in i:
        valor = int(j)
        l.append(valor)

a = min(l)
b = l.index(a)

print("Menor valor:", a)
print("Posicao:", b)