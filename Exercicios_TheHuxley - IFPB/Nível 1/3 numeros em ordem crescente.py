n = int(input())
n2 = int(input())
n3 = int(input())

if n >= n2 >= n3:
    print(n3)
    print(n2)
    print(n)
elif n >= n3 >= n2:
    print(n2)
    print(n3)
    print(n)
elif n2 >= n >= n3:
    print(n3)
    print(n)
    print(n2)
elif n2 >= n3 >= n:
    print(n)
    print(n3)
    print(n2)
elif n3 >= n2 >= n:
    print(n)
    print(n2)
    print(n3)
elif n3 >= n >= n2:
    print(n2)
    print(n)
    print(n3)
