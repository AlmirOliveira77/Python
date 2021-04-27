media = 1
id = 100
soma = 0
cont = 0
nao = 0
no = []
menor = 0

while True:
   media = int(input())
   if media >= 70:
       cont += 1
   if media < 0:
        break

   nome = input()

   idade = int(input())

   curso = input()

   if (curso == "f") and (media >= 70):
       soma += 1

   if (curso == "s") and (idade >= 18) and (media < 70):
       nao += 1

   if idade < id:
       id = idade
       no.append(nome)




a = len(no)

print("Quantidade de aprovados em filosofia :", soma)

if a > 0:
    print("O nome da pessoa mais jovem :", no[-1])

print("Quantidade de aprovados :", cont)

print("Quantidade pessoas maiores de idade nao aprovadas em sociologia :" , nao)

