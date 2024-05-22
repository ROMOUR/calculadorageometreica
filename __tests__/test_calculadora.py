import pytest
from test_calculadora import calcular_area_de_um_cuadrado, calcular_area_de_um_retangulo, calcular_area_de_um_triangulo

# Casos de prueba para calcular_area_de_um_cuadrado
def test_calcular_area_de_um_cuadrado_lado_5():
    assert calcular_area_de_um_cuadrado(5) == 25

def test_calcular_area_de_um_cuadrado_lado_10():
    assert calcular_area_de_um_cuadrado(10) == 100

# Casos de prueba para calcular_area_de_um_retangulo
def test_calcular_area_de_um_retangulo_base_5_altura_4():
    assert calcular_area_de_um_retangulo(5, 4) == 20 

def test_calcular_area_de_um_retangulo_base_10_altura_3():
    assert calcular_area_de_um_retangulo(10, 3) == 30 

# Casos de prueba para calcular_area_de_um_triangulo
def test_calcular_area_de_um_triangulo_base_6_altura_8():
    assert calcular_area_de_um_triangulo(6, 8) == 24

def test_calcular_area_de_um_triangulo_base_10_altura_5():
    assert calcular_area_de_um_triangulo(10, 5) == 25