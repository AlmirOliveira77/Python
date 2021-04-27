sexo = input()
altura = float(input())

if altura > 0:
    if sexo == "m" or sexo == "f":
        if sexo == "m":
            ideal = (72.7 * altura) - 58
            print(round(ideal, 2))
        else:
            ideal = (62.1 * altura) - 44.7
            print(round(ideal, 2))
    else:
        print("O sexo informado eh invalido.")
else:
    print("Altura invalida.")