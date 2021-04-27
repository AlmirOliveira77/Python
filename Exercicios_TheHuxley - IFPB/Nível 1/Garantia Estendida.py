valor = float(input())
gara = int(input())

if gara == 0:
    print("%.2f" % valor)

elif gara == 1:
    total = (valor * 0.03) + valor
    print("%.2f" % total)

elif gara == 2:
    total = (valor * 0.05) + valor
    print("%.2f" % total)
