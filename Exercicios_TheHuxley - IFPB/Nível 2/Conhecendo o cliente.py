continuar = "s"
total = 0
idade_l = []
vendas = 0
cartao = 0
compra =[]
soma = 0

while continuar == "s":

   if continuar !="s":
        break

   idade = int(input())
   idade_l.append(idade)
   valor = float(input())
   compra.append(valor)
   tipo = input().lower()
   proseguir = input().lower()
   continuar = proseguir
   if proseguir == "s":
       vendas += 1

   if tipo == "v":
       total += valor
       soma += 1

   if  tipo == "c":
       cartao += valor


print(vendas+1)
print(round(total, 2))
print(round(cartao,2))
print(min(idade_l))
a = (max(compra))
print(round(a,2))
if total > 0:
    med=total/soma
    print(round(med,2))
else:
    print("0")