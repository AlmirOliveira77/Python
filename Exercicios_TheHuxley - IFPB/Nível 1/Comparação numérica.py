a = "Digite um numero:"
b = "Digite outro numero:"

num1 = int(input(a))
print()
num2 = int(input(b))
print()

if num1 > num2:
    print("Maior numero:", num1)
else:
    print("Maior numero:", "%.1f" % num2)