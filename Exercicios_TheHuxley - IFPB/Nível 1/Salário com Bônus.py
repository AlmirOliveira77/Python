nome = input()
salario = float(input())
vendas = float(input())

if vendas > 0:
    total = ((vendas * 0.15) + salario)
    print("TOTAL = R$", "%.2f" % total)

elif vendas == 0:
    print("TOTAL = R$", "%.2f" % salario)