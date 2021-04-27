lista = []

for i in range(3):
    num = int(input())
    lista.append(num)

lista.sort(reverse=True)

for j in lista:
    print(j)