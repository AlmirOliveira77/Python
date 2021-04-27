def soma(num1, num2):
    cont = 0
    if num1 < 0:
        num1 = num1 * -1
        for i in range(num1):
            cont += num2
        cont = cont * -1
    else:
        for i in range(num1):
            cont += num2

    return cont

valor1 = int(input())
valor2 = int(input())

x = soma(valor1, valor2)
print(x)