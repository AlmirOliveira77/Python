a = "Informe o salario do colaborador:"
b = "Salario antes do reajuste:"
c = "Valor do aumento:"
d = "Salario com reajuste:"

e = "Percentual de aumento aplicado: 20%"
f = "Percentual de aumento aplicado: 15%"
g = "Percentual de aumento aplicado: 10%"
h = "Percentual de aumento aplicado: 5%"

salario = float(input(a))
print("")

if salario >= 0 and salario <= 280:
    print(b, salario)
    print (e)
    print(c, salario * 0.2)
    print (d, "%.2f" % (salario * 1.2))

elif salario > 280 and salario <= 700:
    print(b, salario)
    print (f)
    print(c, salario * 0.15)
    print (d, "%.2f" % (salario * 1.15))

elif salario > 700 and salario <= 1500:
    print(b, salario)
    print (g)
    print(c, salario * 0.1)
    print (d, "%.2f" % (salario * 1.1))

else:
    print(b, salario)
    print(h)
    print(c, salario * 0.05)
    print(d, "%.2f" % (salario * 1.05))

