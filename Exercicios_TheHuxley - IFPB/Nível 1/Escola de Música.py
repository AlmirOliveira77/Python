def escola_de_musica(nota, faltas):
    if faltas > 10:
        situacao = "REPROVADO POR FALTAS"
    elif faltas <= 10 and nota >= 9.5:
        situacao = "APROVADO COM LOUVOR"
    elif faltas <= 10 and nota >= 7 and nota < 9.5:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    return situacao

a = float(input())
b = int(input())

x = escola_de_musica(a, b)
print(x)