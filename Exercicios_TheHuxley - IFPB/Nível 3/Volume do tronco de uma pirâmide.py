import math

altura = int(input())
menor = int(input())
maior = int(input())

area_maior = maior ** 2
area_menor = menor ** 2


a = math.sqrt(area_maior)
b = math.sqrt(area_menor)

volume = ((altura / 3) * (area_maior + (a * b) + area_menor))

print(round(volume, 1))