lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

if lado1 == lado2 and lado2 == lado3:
    print("equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("escaleno")
else:
    print("isosceles")