def volume(raio):
    v = (((4 * 3.1416)* raio ** 3) / 3)
    return v

for i in range(3):
    r = float(input())
    x = volume(r)
    print("%.2f" % x)