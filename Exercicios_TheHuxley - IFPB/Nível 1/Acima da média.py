soma  = 0
num1 = float(input())
num2 = float(input())
num3 = float(input())

media = (num1 + num2 + num3) / 3

if num1 <= 10 and num2 <= 10 and num3 <= 10:
  
  if num1 > media:
        soma += 1
  if num2 > media:
        soma += 1
  if num3 > media:
        soma += 1

print(soma)