numero = int(input())

for i in range(numero):
    tamanho = int(input())
    senha = input()

    parar = ""
    for i in range(tamanho):
        parar = parar + "0"

    posicao = 0
    acerto = 0
    indice = 0

    e = 0
    b = 0
    a = 0

    while True:
        resposta = input()

        if resposta == parar:
            break

        elif resposta == senha:
            tamanho = str(tamanho)
            print("("+tamanho+",0"")")
            break


        else:
            analizados = []
            for i in range(len(senha)):
                if senha[i] == resposta[i]:
                    e += 1
                    analizados.append(senha[i])
                elif resposta[i] in senha:
                    if resposta[i] in senha and resposta[i] not in analizados:
                        b += 1

        e = str(e)
        b = str(b)



        print("("+e+","+b+")")
        e = 0
        b = 0