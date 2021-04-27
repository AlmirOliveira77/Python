num = int(input())
cont = 1
s = 0
ant = 4
l = []
A1 = 0
B1 = 0

while cont < num+1:
    if cont % 2 != 0:
        s += (1+A1) / (4+B1)
        A1 += 2
        B1 += 4
    else:
        s += 1
    cont += 1

if num == 0:
    print(0.0)

else:
    for i in range(1, num + 1):
        if i%2==0:
            valor = '1'
            l.append(valor)
            l.append(' + ')
        elif i == 1:
            valor = '1/4'
            l.append(valor)
            l.append(' + ')
        else:
            ant += 4
            valor = (str(i) + '/' + str(ant))
            l.append(valor)
            l.append(' + ')

    l.pop()

if num != 0:
    print('')
    print(round(s,2))

for i in range(len(l)):
    print(l[i],end='')