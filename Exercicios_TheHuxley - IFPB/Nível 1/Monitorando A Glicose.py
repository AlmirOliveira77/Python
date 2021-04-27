soma = 0
soma_num = 0

while True:
    a = int(input())
    soma = soma + a
    soma_num = soma_num + 1
    if a == 0:
        break
soma_num = soma_num - 1

media = soma /  soma_num

if media < 110:
    print("Glicose Normal")

elif media >= 200:
    print("Glicose Muito Alta")

else:
    print("Glicose Alterada")