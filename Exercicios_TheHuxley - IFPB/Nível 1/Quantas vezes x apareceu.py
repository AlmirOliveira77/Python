lista = []
soma = 0

for i in range(11):
    num = int(input())
    lista.append(num)
a = lista[10]

for j in lista:
    if j == a:
        soma += 1

print(soma - 1)