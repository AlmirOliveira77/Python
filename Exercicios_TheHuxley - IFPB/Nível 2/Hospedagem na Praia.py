def CalculaHospedagem(tipo, dias):
    if dias < 3:
        if tipo == "individual":
            total = dias * 125
        elif tipo == "su�te dupla":
            total = dias * 140
        else:
            total = dias * 180
    else:
        if tipo == "individual":
            total = (dias * 125) * 0.85
        elif tipo == "su�te dupla":
            total = (dias * 140) * 0.85
        else:
            total = (dias * 180) * 0.85

    return total

a = input().lower()
b = int(input())

x = CalculaHospedagem(a, b)
print("%.2f" % x)

