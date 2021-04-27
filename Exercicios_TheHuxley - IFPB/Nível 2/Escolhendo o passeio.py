cinema = 0
boliche = 0

for i in range(7):
    passeio = input()
    escolha = passeio.lower()
    if escolha == "cinema":
        cinema += 1
    elif escolha == "boliche":
        boliche += 1

if cinema > boliche:
    print("CINEMA")
else:print("BOLICHE")