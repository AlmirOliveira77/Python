def CalculaMulta(velocidade):
    limite = 50

    if velocidade > limite:
        if velocidade <= limite * 1.1:
            multa = 230.00
        elif velocidade > limite * 1.1 and velocidade <= limite * 1.2:
            multa = 340.00
        else:
            multa = (velocidade - 50) * 19.28
    else:
        multa = 0.00

    return multa

carro = int(input())

x = CalculaMulta(carro)
print("%.2f" % x)