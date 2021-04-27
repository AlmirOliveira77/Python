escala = input()
temp = float(input())

if (escala == "C" and temp >= -273) or (escala == "K" and temp >= 0) or (escala == "F" and temp >= -459.67):

    if escala == "C" and temp >= -273:
        f = ((1.8 * temp) + 32)
        k = temp + 273
        print(round(f, 2),"F")
        print(round(k, 2),"K")


    elif escala == "K" and temp >= 0:
        c = temp - 273
        f = ((1.8 * c) + 32)
        print(round(c, 2),"C")
        print(round(f, 2),"F")


    elif escala == "F" and temp >= -459.67:
        c = (temp - 32) / 1.8
        k = c + 273
        print(round(c, 2),"C")
        print(round(k, 2),"K")

else:
    print("Valor de temperatura abaixo do minimo")
