def eh_primo(num):
    cont = 0

    for i in range(1, num + 1):
        if num % i == 0:
            cont +=1
    return cont == 2

def produto(l):
    soma = 0
    prod = 1
    for i in l:
        if(eh_primo(i)):
            prod *= i
            soma +=1
    if soma == 4:
        return prod
    else:
        prod = "SEM PRODUTO"
    return prod


primos = []

a, b, c, d = map(int, input().split())

l = [a,b,c,d]

q = produto(l)
print(q)

