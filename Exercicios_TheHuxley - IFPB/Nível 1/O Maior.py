def maior(num1, num2, num3):
    parcial = ((num1 + num2 + abs(num1 - num2)) / 2)
    total = ((parcial + num3 + abs(parcial - num3)) / 2)

    return total

a, b, c = map(int, input().split())
x = maior(a,b,c)
print(int(x), "eh o maior")