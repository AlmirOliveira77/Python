vogal = input()

if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u" or vogal == "A" or vogal == "E" or vogal == "I" or vogal == "O" or vogal == "U":
    print("Eh vogal")

elif len(vogal) > 1:
    print("1 caractere, por favor!")

else:
    print("Nao eh vogal")