num = int(input())
a = 0
b = 0
c = 0
for i in range(num):
    a+=1
    b+=3
    c +=a/b
    if i == num-1:
        print(str(a)+"/"+str(+b))
    else:
        print(str(a)+"/"+str(+b),end=" + ")
if num == 0:
    print(float(num))
else:
    print(round(c,2))