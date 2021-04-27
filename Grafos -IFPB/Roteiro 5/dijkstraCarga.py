def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    verificacao = 0

    while (w != v):
        verificacao2 = 0
        for ligacoes in arestas:
            if (ligacoes[0] == w):
                if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + 1:
                    beta[ligacoes[2]] = beta[w] + 1
                    pi[ligacoes[2]] = w
                    verificacao2 += 1

        minimoBeta = float('inf')
        for vertice in vertices:
            if phi[vertice] == 0 and beta[vertice] < float('inf'):
                if beta[vertice] < minimoBeta:
                    minimoBeta = beta[vertice]

        if verificacao2 == 0 and minimoBeta == float('inf'):
            verificacao += 1
            break

        for vertice in vertices:
            if beta[vertice] == minimoBeta and phi[vertice] == 0 and beta[vertice] < float('inf'):
                phi[vertice] = 1
                w = vertice
                break

    if verificacao == 1:
        return False

    else:
        # PEGANDO OS ANTECESSORES
        atual = v
        lista = []
        while atual != u:
            for aaa in pi:
                if aaa == atual:
                    lista.append(atual)
                    atual = pi[atual]
                    break

        lista.append(atual)

        return len(lista) - 1, lista[::-1]


def DijkstraCarga(vertices, arestas, u, v, carga, pontosRecarga):
    inicial = u
    pontosRecarga.insert(0, u)
    pontosRecarga.append(v)
    possibilidades = {}

    for i in range(len(pontosRecarga)):
        for j in range(len(pontosRecarga)):
            if u == pontosRecarga[j] or dijkstra(vertices, arestas, u, pontosRecarga[j]) == False:
                continue
            caminho = dijkstra(vertices, arestas, u, pontosRecarga[j])[0]
            if caminho <= carga:
                possibilidades[u + "-" + pontosRecarga[j]] = caminho
        u = pontosRecarga[i]
        if i > 0:
            carga = 5

    lista = dijkstra(pontosRecarga, possibilidades, inicial, v)

    if lista == False:
        return "Não há caminho possível !!"

    caminhoFinal = []
    for i in range(len(lista[1])-1):
        caminhoFinal.append(dijkstra(vertices, arestas, lista[1][i], lista[1][i+1])[1])

    Final = []

    for i in range(len(caminhoFinal)):
        for j in range(len(caminhoFinal[i])):
            if (caminhoFinal[i][j] not in Final):
                Final.append(caminhoFinal[i][j])

    return Final