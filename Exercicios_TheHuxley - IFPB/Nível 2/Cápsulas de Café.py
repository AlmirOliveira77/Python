quant_p = 0
quant_g = 0

for i in range (0 , 7):
    quant = int(input())
    tamanho = input()

    if tamanho == "p" or tamanho == "P":
        quant_p += quant * 10
    else:
        quant_g += quant * 16

total = quant_g + quant_p
xicara = (total * 2) / 7

beber  = int(xicara)

print(total)
print(beber)



