a = "A"
b = "B"
c = "C"
d = "D"

livros = int(input())
alunos = int(input())

cla = livros / alunos

if cla >= 1/8:
    print(a)

elif cla <= 1/9 and cla >= 1/12:
    print(b)

elif cla <= 1/13 and cla >= 1/18:
    print(c)

elif cla < 1/18:
    print(d)