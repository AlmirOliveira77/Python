massa = float(input())
altura = float(input())

imc = (massa / (altura**2))

if imc <= 18.5:
    print("%.2f" % imc, "MAGREZA")

elif imc > 18.5 and imc <= 24.9:
    print("%.2f" % imc, "SAUDAVEL")

elif imc > 25 and imc < 29.9:
    print("%.2f" % imc, "SOBREPESO")

elif imc > 30:
    print("%.2f" % imc, "OBESIDADE")