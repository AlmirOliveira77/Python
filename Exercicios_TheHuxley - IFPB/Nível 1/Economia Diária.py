valor = float(input())
total = valor
dias = 0

for i in range(6):
    num = float(input())
    total += num
    if num >= valor + 0.50:
        dias += 1
    valor = num

print("R$", "%.2f" % total)
print(dias)