cont = 0

while True:
    pt = int(input())
    if pt < 0:
        break
    mat = int(input())
    red = float(input())
    if pt >= 40 and mat >= 21 and red >=7:
        cont += 1

print(cont)