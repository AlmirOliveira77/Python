altura, idade = map(float, input().split())

soma = 0

if altura >= 150 and idade >=12:
    soma = soma + 1
if altura >= 140 and idade >= 14:
    soma = soma + 1
if altura >= 170 or idade >= 16:
    soma = soma + 1

print(soma)