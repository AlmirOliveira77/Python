cont_sh = 0
cont_sm = 0
m = 0
f = 0
sex = []
sal = []

for i in range(10):
   salario = float(input())
   sal.append(salario)
   sexo = input()
   sex.append(sexo)
   if sexo == "m":
       m += 1
       cont_sh += salario
   else:
       f += 1
       cont_sm += salario


print(m)
print(f)
media = (cont_sm + cont_sh)/(f + m)
print(round(media, 2))
a = max(sal)
b = sal.index(a)
print(sex[b])
media_2 = (cont_sh / m)
print(round(media_2, 2))
