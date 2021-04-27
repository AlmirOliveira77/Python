lista = []
num = 1

while True:
    num = int(input())
    if num == 0:
        break

    for i in range(num):
        nome = input()
        lista.append(nome)
    lista.sort()

    for i in lista:
        print(i)

    lista.clear()



