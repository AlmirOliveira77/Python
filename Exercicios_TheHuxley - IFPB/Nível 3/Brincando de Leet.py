def leet_erro(nome):
    e = ""
    l = ["0","1","2","3","4","5","6","7","8","9"]
    for i in l:
        if i in nome:
            e = "numeros" "\n" "0"
        elif nome == " ":
            e = "leet" "\n" "0"
    return e

def leet_troca(nome):

    nome = nome.replace("a", "@")
    nome = nome.replace("e", "3")
    nome = nome.replace("i", "1")
    nome = nome.replace("o", "0")
    nome = nome.replace("t", "7")
    nome = nome.replace("s", "5")

    final = nome

    return final

def leet_soma(nome):
    soma = 0
    if leet_erro(nome):
        soma = leet_erro(nome)
    else:
        for i in nome:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "t" or i == "s":
                soma += 1
        a = leet_troca(nome)
        l = [a[::-1], (soma)]
        print(l[0])


    return soma


valor = input().lower()
x = leet_soma(valor)
print(x)












