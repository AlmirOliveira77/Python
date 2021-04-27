a = 0
b = 0
c = 0
brancos = 0
nulos = 0
mais = []

while True:
    secao = int(input())
    if secao == 0:
        break

    ca = int(input())
    a += ca

    cb = int(input())
    b += cb

    cc = int(input())
    c += cc

    cbrancos = int(input())
    brancos += cbrancos

    cnulos = int(input())
    nulos += cnulos

print("Numero de votantes:", a + b + c + brancos + nulos)
print("Total A:", a)
print("Total B:", b)
print("Total C:", c)
print("Brancos:", brancos)
print("Nulos:", nulos)
print("Validos:", a + b + c)

mais.append(a)
mais.append(b)
mais.append(c)



if (a > 0 or b > 0 or c > 0) and (a != b and b != c):
    if max(mais) == a:
        print("Candidato mais votado: A")
    elif max(mais) == b:
        print("Candidato mais votado: b")
    else:
        print("Candidato mais votado: C")
else:
    print("Candidato mais votado: ")

if a + b + c > nulos + brancos:
    print("Eleicao valida? True")
else:
    print("Eleicao valida? False")

if a > 0 or b > 0 or c > 0:
    if max(mais) >= ((a + b + c) / 2):
        print("Segundo turno? False")
    else:
        print("Segundo turno? True")
else:
    print("Segundo turno? False")