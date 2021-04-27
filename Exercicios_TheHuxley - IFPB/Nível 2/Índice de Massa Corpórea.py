massa = float(input())
altura = float(input())

imc = ((massa) / (altura ** 2))

if imc < 17:
    print("muito abaixo do peso")

elif imc > 17 and imc <= 18.49:
    print("abaixo do peso")

elif imc >= 18.5 and imc <= 24.99:
    print("peso normal")

elif imc > 25 and imc <= 29.99:
    print("acima do peso")

elif imc > 30 and imc <= 34.99:
    print("obesidade")

elif imc > 35 and imc <= 39.99:
    print("obesidade severa")

elif imc > 40:
    print("obesidade morbida")