entrada = input().split(" ") #Recebendo o numero de linhas e colunas pelo espa�o.
linhas, colunas = int(entrada[0]), int(entrada[1]) #Atribuindo os termos de linhas e colunas para vari�veis
matriz = [] #Iniciando a matriz vazia
soma_diagPrincipal = 0
soma_diagSecundaria = 0
maior_zero = 0
menor_zero = 0

#For realizado para preencher a matriz
for i in range(linhas):
    linhas1 = []
    for j in range(colunas):
        entrada2 = int(input())
        linhas1.append(entrada2)
    matriz.append(linhas1)
print("Matriz formada:")

#For utilizado para printar a matriz conforme a quest�o.
for i in range(linhas):
    contatena = ""
    for j in range(colunas):
        if matriz[i][-1] != matriz[i][j]:
            contatena += str(matriz[i][j])
            contatena += " "
        else:
            contatena += str(matriz[i][j])
    print(contatena)

#For utilizado para atribuir os valores da quest�o.
for i in range(linhas):
    for j in range(colunas):
        if i == j: #DIAGONAL PRINCIPAL
            soma_diagPrincipal += matriz[i][j]
        if   j == (linhas - 1 - i): #DIAGONAL SECUNDARIA
            soma_diagSecundaria += matriz[i][j]
        if matriz[i][j] > 0: #NUMEROS MAIORES QUE ZERO
            maior_zero += 1
        if matriz[i][j] < 0: #NUMEROS MENORES QUE ZERO
            menor_zero += 1

if linhas == colunas:
    print("A diagonal principal e secundaria tem valor(es) %i e %i respectivamente."%(soma_diagPrincipal,soma_diagSecundaria))
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")

print("A matriz possui %i numero(s) menor(es) que zero."%(menor_zero))
print("A matriz possui %i numero(s) maior(es) que zero."%(maior_zero))
