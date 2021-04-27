num = float(input())

if num <= num ** 12:
    if num > 0 and num % 2 == 0:
        print("POSITIVO PAR")

    elif num > 0 and num % 2 != 0:
        print("POSITIVO IMPAR")

    elif num < 0 and num % 2 == 0:

        print("NEGATIVO PAR")


    elif num < 0 and num % 2 != 0:

        print("NEGATIVO IMPAR")

    else:
        print("NULO")