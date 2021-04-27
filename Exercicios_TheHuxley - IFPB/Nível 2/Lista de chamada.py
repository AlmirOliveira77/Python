num, sort = map(int, input().split())
lista = ["a"]
for i in range(num):
    nome = input()
    lista.append(nome)

lista.sort()
print(lista[sort])
