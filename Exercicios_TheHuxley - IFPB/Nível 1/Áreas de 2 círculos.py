a = "Primeiro c�rculo"
b = "Segundo c�rculo"
c = "Iguais"

raio1 = float(input())
raio2 = float(input())

area1 = (3.1415 * (raio1 ** 2))
area2 = (3.1415 * (raio2 ** 2))

if area1 > area2:
    print(a)
elif area2 > area1:
    print(b)

else:
    print(c)