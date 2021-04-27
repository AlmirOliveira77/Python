l = []
soma = []
cont = 0

for i in range(5):
    num = int(input())
    l.append(num)

    for j in range(1, num + 1):
        if num % j == 0:
            cont += j

    soma.append(cont)
    cont = 0

a = max(soma)
b = soma.index(a)

print(l[b])

