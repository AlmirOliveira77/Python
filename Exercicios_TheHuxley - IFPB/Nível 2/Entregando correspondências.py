cont = 0
soma = 0

for i in range(7):
    num = int(input())
    soma += num
    if num >= 100:
        cont += 1
media = soma / 7

print(cont)
print(int(media))
