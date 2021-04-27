mulher = int(input())
homem = int(input())

gasto_m = mulher * 10
gasto_h = homem * 8.50

media = ((gasto_h + gasto_m) / (homem + mulher))

print("%.2f" % (gasto_h + gasto_m))
print("%.2f" % media)