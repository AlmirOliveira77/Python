while True:
    mult = int(input())
    if mult == 0:
        break
    m = [[], [], [], []]
    for i in m:
        num1 = int(input())
        i.append(num1)
        num2 = int(input())
        i.append(num2)
        num3 = int(input())
        i.append(num3)
        num4 = int(input())
        i.append(num4)

    for i in range(len(m[0])):
        for j in range(len(m[i])):
            if i == j:
                m[i][j] = (m[i][j]) * mult

            print("%1d" % m[j][i], end=" ")
        print()