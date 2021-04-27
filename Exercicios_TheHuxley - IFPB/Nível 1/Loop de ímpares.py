lista = []
num = int(input())
num2 = int(input())
num2 = num2 + 1

for i in range(num, num2):
    if i % 2 != 0:
        lista.append(i)

for j in lista:
    print(j)




