fat = 1

while True:
    num = int(input())
    if num  == -1:
        break
    for i in range(1, num + 1):
        fat = fat * i
    print(fat)
    fat = 1
