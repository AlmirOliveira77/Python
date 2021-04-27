temp = float(input())
secre = input()

if temp >= 35 and temp <= 41 and secre == "S" or secre == "N":

    if temp >= 37 and secre == "S":
        print("Exames Especiais")

    elif temp >= 37 and secre == "N":
        print("Exames Basicos")

    elif temp <= 37 and secre == "N":
        print("Liberado")

    elif temp <= 37 and secre == "S":
        print("Exames Basicos")

else:
    print("Erro")