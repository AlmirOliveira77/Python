alibaba = 0
alcapone = 0
branco = 0
nulo = 0
while True:
    votos = int(input())
    if votos == -1:
        break
    if votos == 83:
        alibaba += 1
    elif votos == 93:
        alcapone += 1
    elif votos == 0:
        branco += 1
    else:
        nulo += 1

print(alibaba)
print(alcapone)
print(branco)
print(nulo)
if alibaba > alcapone:
    print("83")
else:
    print("93")
validos = alibaba + alcapone + branco
por_a = (alibaba * 100) / validos
por_b = (alcapone * 100) / validos

print("%.2f" % por_a)
print("%.2f" % por_b)