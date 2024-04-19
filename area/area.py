# test_areas.py
import pytest
import math
from area.area import area_quadrado, area_retangulo, area_triangulo, area_circulo

# Testes para a função area_circulo
def test_area_circulo_raio_1():
    assert math.isclose(area_circulo(1), math.pi)

def test_area_circulo_raio_2():
    assert math.isclose(area_circulo(2), 4 * math.pi)