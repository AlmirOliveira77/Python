import math
soma = 0

while True:
    num = int(input())
    soma = soma + num
    if num % 2 != 0:
        soma = soma - num
        break

final = soma / 12
a = math.ceil(final)
valor = a * 7.89
final_r = (a * 12) - soma

print(valor)
print(final_r)
