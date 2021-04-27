soma = 0

a = "Telefonou para a vitima?"
b = "Esteve no local do crime?"
c = "Mora perto da vitima?"
d = "Devia para a vitima?"
e = "Ja trabalhou com a vitima?"

per1 = input(a)
print()
per2 = input(b)
print()
per3 = input(c)
print()
per4 = input(d)
print()
per5 = input(e)
print()

if per1 == "True":
    soma += 1
if per2 == "True":
    soma += 1
if per3 == "True":
    soma += 1
if per4 == "True":
    soma += 1
if per5 == "True":
    soma += 1

if soma < 2:
    print("Inocente")
elif soma == 2:
    print("Suspeita")
elif soma >= 3 and soma < 4:
    print("Cumplice")
elif soma == 5:
    print("Assassino")
