import math

temperatura = float(input())
massa = float(input())

a = (((3 * 8.31) * temperatura) / massa)
velocidade = math.sqrt(a)

print(round(velocidade, 2))
