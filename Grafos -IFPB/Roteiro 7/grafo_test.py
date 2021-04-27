from grafo_adj import *
from grafo_adj_nao_dir import *
import unittest

class TestGrafo(unittest.TestCase):

    def setUp(self):

        self.direcionado = Grafo([], [])
        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
            self.direcionado.adiciona_vertice(i)
        for i in ['1-2', '1-7', '1-4', '7-5', '7-3', '7-3', '5-4', '5-6', '6-7', '3-2', '3-4', '8-3', '8-9', '9-12', '9-13', '10-9', '11-10', '11-9', '11-12', '13-12', '13-8']:
            self.direcionado.adiciona_aresta(i)

        self.direcionado2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            self.direcionado2.adiciona_vertice(i)
        for i in ['A-D', 'A-G', 'A-B', 'B-C', 'C-D', 'C-E', 'E-B', 'B-F', 'B-F', 'F-D', 'F-G', 'K-F', 'K-I', 'I-J', 'I-L', 'J-K', 'J-L', 'M-H', 'M-I', 'M-L', 'H-I']:
            self.direcionado2.adiciona_aresta(i)

        self.nao_direcionado = Grafo_nao_direcionado([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            self.nao_direcionado.adicionaVertice(i)
        for i in ['A-H', 'A-J', 'A-B', 'H-C', 'H-D', 'H-E', 'H-F', 'H-B', 'B-G', 'B-J', 'B-K', 'G-F', 'B-I', 'I-J', 'J-K', 'D-C', 'D-E']:
            self.nao_direcionado.adicionaAresta(i)

        self.nao_direcionado2 = Grafo_nao_direcionado([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            self.nao_direcionado2.adicionaVertice(i)
        for i in ['A-B','A-J','A-H','B-C','B-D','B-E','B-F','H-B','H-G','H-J','H-K','G-F','H-I','I-J','J-K','D-C','D-E']:
            self.nao_direcionado2.adicionaAresta(i)


    def test_grafo_direcionado(self):
        self.assertEqual(self.direcionado.grafo_direcionado(), (['1-2', '1-4', '1-7', '7-3', '7-5', '5-6', '8-9', '9-12', '9-13'], ['7-3', '6-7', '13-8'], ['3-2', '3-4', '5-4', '8-3', '13-12', '10-9', '11-9', '11-10', '11-12']))
        self.assertEqual(self.direcionado2.grafo_direcionado(), (['A-B', 'B-C', 'C-D', 'C-E', 'B-F', 'F-G', 'H-I', 'I-J', 'J-K', 'J-L'], ['E-B', 'B-F', 'A-D', 'A-G', 'K-I', 'I-L'], ['F-D', 'K-F', 'M-H', 'M-I', 'M-L']))

    def test_grafo_nao_direcionado(self):
        self.assertEqual(self.nao_direcionado.grafo_nao_direcionado(), (['A-B', 'B-G', 'G-F', 'F-H', 'H-C', 'C-D', 'D-E', 'B-I', 'I-J', 'J-K'], ['H-A', 'H-B', 'E-H', 'D-H', 'J-A', 'J-B', 'K-B']))
        self.assertEqual(self.nao_direcionado2.grafo_nao_direcionado(), (['A-B', 'B-C', 'C-D', 'D-E', 'B-F', 'F-G', 'G-H', 'H-I', 'I-J', 'J-K'], ['D-B', 'E-B', 'H-A', 'H-B', 'J-A', 'J-H', 'K-H']))
