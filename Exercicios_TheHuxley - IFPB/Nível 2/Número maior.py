lista = []
a = "Digite um numero:"
b = "Digite outro numero:"


num = int(input(a))
print()
lista.append(num)
num2 = int(input(b))
print()
lista.append(num2)
num3 = int(input(b))
print()
lista.append(num3)

lista.sort(reverse=True)
d = lista[0]

print("Maior numero:",float(d))