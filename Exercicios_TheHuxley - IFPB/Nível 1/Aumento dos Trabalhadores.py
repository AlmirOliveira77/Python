salario = float(input())

if salario >= 500:
    print("%.2f" % (salario * 1.1))

elif salario >= 300 and salario < 500:
    print("%.2f" % (salario * 1.07))

else:
    print("%.2f" % (salario * 1.05))