lista = []
num1 = int(input())
num2 = int(input())
soma = 0

if num1 < num2:
    a = num1
    b = num2 + 1
    for i in range(a, b):
        lista.append(i)
else:
    a = num1 + 1
    b = num2
    for i in range(b, a):
        lista.append(i)

for j in lista:
    if j > 0:
        soma += j

print(soma)