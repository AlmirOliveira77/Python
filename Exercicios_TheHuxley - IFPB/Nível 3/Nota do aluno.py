soma = 0

a = "Insira a resposta do aluno para a pergunta 1:"
b = "Insira a resposta do aluno para a pergunta 2:"
c = "Insira a resposta do aluno para a pergunta 3:"
d = "Insira a resposta do aluno para a pergunta 4:"
e = "Insira a resposta do aluno para a pergunta 5:"
f = "Insira a resposta do aluno para a pergunta 6:"
g = "Insira a resposta do aluno para a pergunta 7:"
h = "Insira a resposta do aluno para a pergunta 8:"
i = "Insira a resposta do aluno para a pergunta 9:"
j = "Insira a resposta do aluno para a pergunta 10:"

nota1 = input(a)
print()
nota2 = input(b)
print()
nota3 = input(c)
print()
nota4 = input(d)
print()
nota5 = input(e)
print()
nota6 = input(f)
print()
nota7 = input(g)
print()
nota8 = input(h)
print()
nota9 = input(i)
print()
nota10 = input(j)
print()

if nota1 == "A":
    soma += 1
if nota2 == "B":
    soma += 1
if nota3== "C":
    soma += 1
if nota4 == "D":
    soma += 1
if nota5 == "E":
    soma += 1
if nota6 == "E":
    soma += 1
if nota7 == "D":
    soma += 1
if nota8 == "C":
    soma += 1
if nota9 == "B":
    soma += 1
if nota10 == "A":
    soma += 1

print("Nota do aluno:", soma)