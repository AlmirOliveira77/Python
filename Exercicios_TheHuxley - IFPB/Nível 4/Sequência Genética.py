tp = int(input())
ts = int(input())
base = input()
c = len(base)
ps1 = input()
ps2 = input()

if tp + ts <= c and tp > 0 and ts > 0:
    a = base[0:tp]
    print(a.upper(), ":")
    print(a + ps1)
    print(a + ps2)
    print()
    b = base[ts:c]
    print(b.upper(), ":")
    print(ps1 + b)
    print(ps2 + b)

else:
    print("TAMANHO INVALIDO")

