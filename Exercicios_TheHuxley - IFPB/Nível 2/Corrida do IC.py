lista = []

a,b,c,d,e = map(int, input().split())

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

lista.sort(reverse=True)

print("1 -", lista[0], "km/h")
print("2 -", lista[1], "km/h")
print("3 -", lista[2], "km/h")
print("4 -", lista[3], "km/h")
print("5 -", lista[4], "km/h")