cv, ce, cs, fv, fe, fs = map(int,input(). split())

pontos_c = (cv * 3) + ce
pontos_f = (fv * 3) + fe


if pontos_c > pontos_f:
    print("C")

if pontos_f > pontos_c:
    print("F")

if pontos_c == pontos_f:

    if cs > fs:
        print("C")
    elif fs > cs:
        print("F")

if pontos_c == pontos_f and cs == fs:
    print("=")
