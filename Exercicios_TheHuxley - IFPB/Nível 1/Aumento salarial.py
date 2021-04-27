salario = float(input())

if salario < 1000:
    print("%.2f" % (salario * 1.3))

elif salario >= 1000 and salario < 2000:
    print("%.2f" % (salario * 1.1))

else:
    print("%.2f" % salario)