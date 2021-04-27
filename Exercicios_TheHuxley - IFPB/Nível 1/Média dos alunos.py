a = float(input())
b = float(input())
c = float(input())

media = ((a + b + c) / 3)

if media < 3:
    print("reprovado")

elif media >= 3 and media < 7:
    print("prova final")

else:
    print("aprovado")