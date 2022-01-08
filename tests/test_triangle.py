from unittest import TestCase
from triangles import *

class TestMatrix(TestCase):
    def test_classifica_equilatero(self):
        classificacao_triangulo = classifica_triangulo(10, 10, 10)
        self.assertEqual(classificacao_triangulo, "Triângulo Equilátero")

    def test_classifica_escaleno(self):
        classificacao_triangulo = classifica_triangulo(10, 9, 8)
        self.assertEqual(classificacao_triangulo, "Triângulo Escaleno")

    def test_classifica_isosceles(self):
        classificacao_triangulo = classifica_triangulo(10, 10, 9)
        self.assertEqual(classificacao_triangulo, "Triângulo Isósceles")

    def test_classifica_nao_existe(self):
        classificacao_triangulo = classifica_triangulo(10, 25, 10)
        self.assertEqual(classificacao_triangulo, "Triângulo não Existe")

    def test_classifica_lados_negativos(self):
        classificacao_triangulo = classifica_triangulo(-10, 10, 10)
        self.assertEqual(classificacao_triangulo, "Triângulo não Existe")

    def test_classifica_lado_zero(self):
        classificacao_triangulo = classifica_triangulo(0, 0, 0)
        self.assertEqual(classificacao_triangulo, "Triângulo não Existe")

    def test_calcula_area_escaleno(self):
        area = calcula_area(10,9,8)
        self.assertEqual(area, 34.20)

    def test_calcula_area_equilatero(self):
        area = calcula_area(15,15,15)
        self.assertEqual(area, 97.43)

    def test_classifica_area_isosceles(self):
        area = calcula_area(10,10,9)
        self.assertEqual(area, 40.19)

    def test_calcula_area_triangulo_inexistente(self):
         area = calcula_area(10,5,20)
         self.assertEqual(area, "Triângulo não Existe")


