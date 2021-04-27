a, b, c = map(float,input().split())

triangulo = (a * c) / 2
circulo = (3.14159 * (c ** 2))
trapezio = (((a + b) * c) / 2)
quadrado = b ** 2
retangulo = a * b

t = "TRIANGULO:"
c = "CIRCULO:"
tr = "TRAPEZIO:"
q = "QUADRADO:"
r = "RETANGULO:"

print(t, "%.3f" % triangulo)
print(c, "%.3f" % circulo)
print(tr, "%.3f" % trapezio)
print(q, "%.3f" % quadrado)
print(r, "%.3f" % retangulo)