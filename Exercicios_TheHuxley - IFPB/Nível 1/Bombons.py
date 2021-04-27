valor_avela = float(input())
valor_caramelo = float(input())
valor_passas = float(input())

avela = float(input())
caramelo = float(input())
passas = float(input())

total = (valor_avela * avela) + (valor_caramelo * caramelo) + (valor_passas * passas)
a = "Valor:"
b = "R$"
c = ("%.2f" % total)
print (a, b + str (c))
