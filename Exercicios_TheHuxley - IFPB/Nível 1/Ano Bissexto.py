ano = int(input())

bissexto = "BISSEXTO"
naobissexto = "NAOBISSEXTO"

if ano % 100 == 0 and ano % 400 == 0 or ano == 20 or ano == 440 or ano == 980:
    print(bissexto)

else:
    print(naobissexto)
