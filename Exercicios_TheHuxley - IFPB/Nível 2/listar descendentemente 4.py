lista = []

a, b, c, d = map(int, input().split())

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)

lista.sort(reverse=True)

print(lista[0], lista[1], lista[2], lista[3])






