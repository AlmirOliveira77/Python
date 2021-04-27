num = int(input())


a = num / 100
ar = num % 100
b = ar / 50
br = ar % 50
c = br / 20
cr = br % 20
d = cr / 10
dr = cr % 10
e = dr / 5
er = dr % 5
f = er / 2
fr = er % 2
g = fr / 1
gr = fr % 1

nota1 = int(a)
nota2 = int(b)
nota3 = int(c)
nota4 = int(d)
nota5 = int(e)
nota6 = int(f)
nota7 = int(g)

print(num)
print(nota1, "nota(s) de R$ 100,00")
print(nota2, "nota(s) de R$ 50,00")
print(nota3, "nota(s) de R$ 20,00")
print(nota4, "nota(s) de R$ 10,00")
print(nota5, "nota(s) de R$ 5,00")
print(nota6, "nota(s) de R$ 2,00")
print(nota7, "nota(s) de R$ 1,00")


