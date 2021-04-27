forma = input()

if forma == "Q":
    q = float(input())
    q_p = q * 4
    q_a = q * q
    print(round(q_a, 2))
    print(round(q_p, 2))

elif forma == "R":
    r_l = float(input())
    r_a = float(input())
    r_p = (r_l * 2) + (r_a * 2)
    r_a = r_a * r_l
    print(round(r_a, 2))
    print(round(r_p, 2))

elif forma == "C":
    raio = float(input())
    c_a = (3.14 * (raio ** 2))
    c_p = ((2 * 3.14)* raio)
    print(round(c_a, 2))
    print(round(c_p, 2))

else:
    print("Nenhuma figura selecionada")
