soma = 0
a = "Foram digitados"
b = "numeros negativos"
c = "Digite um valor:"
for i in range(5):
    num = float(input(c))
    print("")
    if num < 0:
        soma = soma + 1

print(a, soma, b)