num = int(input())
num_2 = int(input())
l = []

soma = 0

if num < num_2:
    a = num
    b = num_2
else:
    a = num_2
    b = num

for i in range(a, b + 1):
    for j in range(1, b +1):
        if i % j == 0:
            soma += 1
    if soma == 2:
        if soma != 1:
            l.append(i)
    soma = 0

l.sort(reverse = True)

for i in l:
    print(i)
