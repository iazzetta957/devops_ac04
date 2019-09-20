from unittest import TestCase
from com.Matheus.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()

    
    def test_mult(self):
        self.assertEqual(self.operacoes.mult([5,5]), 25)