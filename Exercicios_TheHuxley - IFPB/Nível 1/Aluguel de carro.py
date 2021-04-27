diaria = int(input())
km = int(input())

valor = (((diaria * 30) + (km * 0.01))) * 0.1
total = (((diaria * 30) + (km * 0.01))) - valor

print(round(total,2))