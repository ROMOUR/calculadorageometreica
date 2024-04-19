
import pytest 

from area.area import calcular_area_de_um_cuadrado, calcular_area_de_um_retangulo, calcular_area_de_um_triangulo
from utils.utils import ler_csv


def test_area_quadrado_lado_5():
    assert test_area_quadrado_lado_5(5) == 25 

def test_area_quadrado_lado_10():
    assert test_area_quadrado_lado_10(10) == 100

def test_area_retangulo_base_5_altura_4():
    assert test_area_retangulo_base_5_altura_4(5, 4) == 20 

def test_area_retangulo_base_10_altura_3():
    assert test_area_retangulo_base_10_altura_3(10, 3) == 30 

def test_area_triangulo_base_6_altura_8():
    assert test_area_triangulo_base_6_altura_8(6, 8) == 24

def test_area_triangulo_base_10_altura_5():
    assert test_area_triangulo_base_10_altura_5(10, 5) == 25