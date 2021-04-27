num = int(input())

if num >= 10:
    print(num % 10)

elif num >= 0 and num < 10:
    print(num)

elif num < 0:
    print(num % -10)

