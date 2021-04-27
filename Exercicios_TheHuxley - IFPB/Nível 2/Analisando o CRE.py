matricula = []
cre = []
mat = 1
cont = 0

while True:
    mat = input()
    if mat == "999":
        break
    cr = float(input())
    cre.append(cr)
    matricula.append(mat)
    cont += cr


a = len(cre)
media = cont / a

menor_cre = min(cre)
menor = cre.index(menor_cre)

print(matricula[menor])
print("%.2f" % media)

