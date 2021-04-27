while True:
    cont = 0
    num = int(input())
    if num < 0:
        break
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    soma = num

    if cont == 2:
        print("1")
    else:
        print("0")
