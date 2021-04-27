def digitos(valor):
    cont = 0
    for i in range(9 + 1):
        for j in valor:
            a = str(i)
            if a == j:
                cont += 1
    return cont

nome = input()

x = digitos(nome)
print(x)