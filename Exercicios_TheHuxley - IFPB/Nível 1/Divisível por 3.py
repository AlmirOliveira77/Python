lista = []
num = int(input())
a = num + 1
soma = 0

for i in range(1, a):
    if num % i == 0:
        if i % 3 == 0:
            soma += 1

if soma == 0:
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(soma)
