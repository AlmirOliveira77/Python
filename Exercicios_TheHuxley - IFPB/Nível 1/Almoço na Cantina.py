comida = input()
bebida = input()

c = comida.lower()
b = bebida.lower()

if c == "lasanha" and b == "suco":
    print("10.50")
elif c == "lasanha" and b == "refrigerante":
    print("11.00")
elif c == "estrogonofe" and b == "suco":
    print("13.50")
elif c == "estrogonofe" and b == "refrigerante":
    print("14.00")