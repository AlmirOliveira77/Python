dia = input()
preco = float(input())
opcao = input()
nome = input()

if (dia == "seg" or dia == "ter" or dia == "qua") and opcao == "ouro":
    prod = preco / 2
    print("O preco do produto", nome, "no dia", dia, "eh", (round(prod, 2)))

elif (dia == "qui" or dia == "sex" and preco >= 10) and preco <= 100:
    prod = preco / 3
    print("O preco do produto", nome, "no dia", dia, "eh", (round(prod, 2)))

elif (dia == "sab") and opcao == "prata":
    prod = preco * 3
    print("O preco do produto", nome, "no dia", dia, "eh", (round(prod, 2)))

else:
    prod = preco * 2
    print("O preco do produto", nome, "no dia", dia, "eh", (round(prod, 2)))
