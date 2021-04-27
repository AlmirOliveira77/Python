a, b, c, d = map(float, input().split())


media = ((((a * 1) + (b * 2)) + (c * 3) + (d * 4)) / 10)

if media < 3:
    print("reprovado")

elif media >= 3 and media < 7:
    print("prova final")

elif media >= 7 and media < 9 :
    print("aprovado")

elif media >= 9:
    print("aprovado com louvor")
