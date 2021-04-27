lista = []
num = int(input())
num = num +1

for i in range(1, num):
    a = i
    lista.append(a)
    b = i * i
    lista.append(b)
    c = b * i
    lista.append(c)

i0 = 0
i1 = 1
i2 = 2

for i in range(1, num):

    print (lista[i0], lista[i1], lista[i2])

    i0 += 3
    i1 += 3
    i2 += 3


