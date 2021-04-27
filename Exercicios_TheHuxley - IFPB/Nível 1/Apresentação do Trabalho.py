ig, ia, e, i, us = map(int,input().split())

av = "AVALIADO"
zr = "0"
soma = e + i + us

if ig + ia >= 1 and soma == 3:
    print(av)
else:
    print(zr)