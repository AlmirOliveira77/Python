a = "Informe a primeira nota:" "\n"
b = "Informe a segunda nota:" "\n"
c = "Informe a terceira nota:" "\n"
d = "Aprovado com media"
e = "Recuperacao com media"
f = "Reprovado com media"


nota1 = float(input(a))
nota2 = float(input(b))
nota3 = float(input(c))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(d, media)
elif media >= 5 and media < 7:
    print(e, media)
else:
    print(f, media)