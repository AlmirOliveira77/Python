nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

peso1 = float(input())
peso2 = float(input())
peso3 = float(input())

soma_p = peso1 + peso2 + peso3

A = "a:"
P = "p:"
H = "h:"

a = (nota1 + nota2 + nota3) / 3
p = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 +peso3)
h = 3 / (1/nota1 + 1/nota2 + 1/nota3)

print(A,a,)
print(P,p)
print(H,h)

