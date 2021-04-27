lista = []
num = int(input())
num2 = int(input())
num3 = int(input())
num3 += 1

for i in range(num2, num3):
    if i % num == 0:
        lista.append(i)
if len(lista) > 1:
    for j in lista:
        print(j)
else:
    print("INEXISTENTE")