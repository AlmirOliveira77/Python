soma = 0

dia  = int(input())
km = int(input())

valor = 90 * dia
dia = dia * 100


if km <= dia:
    print( "%.2f" % valor)

elif km >= dia:
    print ("%.2f" % (valor + (km  - dia) * 12))
