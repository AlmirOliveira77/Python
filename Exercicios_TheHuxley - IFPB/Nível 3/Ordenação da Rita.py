lista = []

for i in range(3):
    a = int(input())
    lista.append(a)


if lista[0] < 0 or lista[1] < 0 or lista [2] < 0:
    print("Ordenacao cancelada.")

elif lista[0] % 2 != 0:
    lista.sort()
    for j in lista:
        print(j)

else:
    lista.sort(reverse=True)
    for k in lista:
        print(k)
