lista = []
lista_2 = []
inter = []

for i in range(0, 20):
    num = int(input())
    lista.append(num)

for j in range(0, 20):
    num = int(input())
    lista_2.append(num)

for k in lista:
    if k in lista_2 and k not in inter:
        inter.append(k)

inter.sort()
a = len(inter)

if a > 0:
    for l in inter:
        print(l)
else:
    print("VAZIO")
