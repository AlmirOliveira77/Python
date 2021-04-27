tipo = int(input())
acertos = 0
resp = input().split(" ")

for i in resp:
    valor = int(i)
    if valor == tipo:
        acertos += 1

print(acertos)
