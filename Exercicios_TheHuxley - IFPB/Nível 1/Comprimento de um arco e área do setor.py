raio = float(input())
graus = float(input())

if raio >= 1 and raio <= 50 and graus >=0 and graus < 360:
    arco = (2 * (3.14 * raio)) * (graus / 360)
    area = (graus * 3.14 * (raio ** 2)) / 360

    print(round(arco, 2))
    print(round(area, 2))


