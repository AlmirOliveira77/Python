from grafo_adj_nao_dir import *
import unittest

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.g.adicionaVertice(i)
        self.g.adicionaAresta("a-g", 4)
        self.g.adicionaAresta("a-b", 9)
        self.g.adicionaAresta("b-c", 6)
        self.g.adicionaAresta("b-h", 7)
        self.g.adicionaAresta("b-g", 10)
        self.g.adicionaAresta("c-d", 8)
        self.g.adicionaAresta("c-f", 8)
        self.g.adicionaAresta("d-e", 14)
        self.g.adicionaAresta("c-e", 12)
        self.g.adicionaAresta("e-f", 2)
        self.g.adicionaAresta("f-h", 2)
        self.g.adicionaAresta("f-g", 1)

        self.g2 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f']:
            self.g2.adicionaVertice(i)
        self.g2.adicionaAresta("a-b", 9)
        self.g2.adicionaAresta("b-c", 6)
        self.g2.adicionaAresta("c-d", 8)
        self.g2.adicionaAresta("c-f", 8)
        self.g2.adicionaAresta("d-e", 14)
        self.g2.adicionaAresta("c-e", 12)
        self.g2.adicionaAresta("e-f", 2)

        self.g3 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            self.g3.adicionaVertice(i)
        self.g3.adicionaAresta("a-g", 5)
        self.g3.adicionaAresta("a-b", 19)
        self.g3.adicionaAresta("b-c", 16)
        self.g3.adicionaAresta("b-g", 13)
        self.g3.adicionaAresta("c-d", 19)
        self.g3.adicionaAresta("c-f", 1)
        self.g3.adicionaAresta("d-e", 21)
        self.g3.adicionaAresta("c-e", 30)
        self.g3.adicionaAresta("e-f", 15)
        self.g3.adicionaAresta("f-g", 3)

        self.g4 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']:
            self.g4.adicionaVertice(i)
        self.g4.adicionaAresta("a-g", 5)
        self.g4.adicionaAresta("a-b", 19)
        self.g4.adicionaAresta("b-c", 16)
        self.g4.adicionaAresta("b-g", 13)
        self.g4.adicionaAresta("c-d", 19)
        self.g4.adicionaAresta("c-f", 1)
        self.g4.adicionaAresta("d-e", 21)
        self.g4.adicionaAresta("c-e", 30)
        self.g4.adicionaAresta("e-f", 15)
        self.g4.adicionaAresta("f-g", 3)
        self.g4.adicionaAresta("g-m", 5)
        self.g4.adicionaAresta("i-k", 1)
        self.g4.adicionaAresta("a-m", 14)
        self.g4.adicionaAresta("j-l", 9)
        self.g4.adicionaAresta("i-m", 8)
        self.g4.adicionaAresta("f-i", 11)
        self.g4.adicionaAresta("f-h", 10)
        self.g4.adicionaAresta("c-e", 13)
        self.g4.adicionaAresta("e-j", 20)
        self.g4.adicionaAresta("f-k", 19)

        self.g5 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.g5.adicionaVertice(i)
        self.g5.adicionaAresta("a-g", 4)
        self.g5.adicionaAresta("a-b", 9)
        self.g5.adicionaAresta("b-c", 6)
        self.g5.adicionaAresta("b-h", 7)
        self.g5.adicionaAresta("b-g", 10)
        self.g5.adicionaAresta("c-d", 8)
        self.g5.adicionaAresta("c-f", 8)
        self.g5.adicionaAresta("d-e", 14)
        self.g5.adicionaAresta("c-e", 12)
        self.g5.adicionaAresta("e-f", 2)
        self.g5.adicionaAresta("f-h", 2)
        self.g5.adicionaAresta("f-g", 1)

        self.g6 = Grafo([], {})

        self.g6.adicionaVertice('a')
        self.g6.adicionaVertice('b')
        self.g6.adicionaVertice('c')
        self.g6.adicionaVertice('d')
        self.g6.adicionaVertice('e')
        self.g6.adicionaVertice('f')

        self.g6.adicionaAresta("a-b", 9)
        self.g6.adicionaAresta("b-c", 6)

        self.g6.adicionaAresta("c-d", 8)
        self.g6.adicionaAresta("c-f", 8)
        self.g6.adicionaAresta("d-e", 14)
        self.g6.adicionaAresta("c-e", 12)
        self.g6.adicionaAresta("e-f", 2)

        self.g7 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            self.g7.adicionaVertice(i)
        self.g7.adicionaAresta("a-c", 50)
        self.g7.adicionaAresta("a-d", 49)
        self.g7.adicionaAresta("b-f", 55)
        self.g7.adicionaAresta("b-g", 60)
        self.g7.adicionaAresta("c-d", 45)
        self.g7.adicionaAresta("c-g", 52)
        self.g7.adicionaAresta("d-f", 44)
        self.g7.adicionaAresta("c-g", 56)
        self.g7.adicionaAresta("e-f", 10)

        self.g8 = Grafo([], {})
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            self.g8.adicionaVertice(i)
        self.g8.adicionaAresta("a-b", 5)
        self.g8.adicionaAresta("a-e", 12)
        self.g8.adicionaAresta("b-g", 4)
        self.g8.adicionaAresta("b-f", 9)
        self.g8.adicionaAresta("c-d", 10)
        self.g8.adicionaAresta("c-f", 7)
        self.g8.adicionaAresta("d-f", 8)
        self.g8.adicionaAresta("c-e", 10)
        self.g8.adicionaAresta("e-g", 2)
        self.g8.adicionaAresta("f-g", 6)

    def test_prim(self):
        self.assertEqual(self.g.prim("g"), ['f-g', 'e-f', 'h-f', 'a-g', 'b-h', 'c-b', 'd-c'])
        self.assertEqual(self.g2.prim("a"), ['b-a', 'c-b', 'd-c', 'f-c', 'e-f'])
        self.assertEqual(self.g3.prim("c"), ['f-c', 'g-f', 'a-g', 'b-g', 'e-f', 'd-c'])
        self.assertEqual(self.g4.prim("e"), ['f-e', 'c-f', 'g-f', 'a-g', 'm-g', 'i-m', 'k-i', 'h-f', 'b-g', 'd-c', 'j-e', 'l-j'])

    def test_kruskal(self):
        self.assertEqual(self.g3.Kruskal(), ['c-f', 'f-g', 'a-g', 'b-g', 'e-f', 'd-e'])
        self.assertEqual(self.g4.Kruskal(), ['c-f', 'i-k', 'f-g', 'a-g', 'g-m', 'j-l', 'b-g', 'e-f', 'd-e'])
        self.assertEqual(self.g5.Kruskal(), ['f-g', 'e-f', 'a-g', 'b-c', 'c-d', 'd-e'])
        self.assertEqual(self.g6.Kruskal(), ['e-f', 'b-c', 'c-d', 'a-b', 'd-e'])
        self.assertEqual(self.g7.Kruskal(), ['e-f', 'd-f', 'c-d', 'a-d', 'b-f'])
        self.assertEqual(self.g8.Kruskal(), ['e-g', 'b-g', 'a-b', 'f-g', 'c-f', 'd-f'])