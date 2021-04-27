nome = input()
nome_2 = input()

cont = nome.find(nome_2)

if cont >= 0:
    print(cont)
else:
    print("-1")