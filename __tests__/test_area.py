from typing import Literal
import pytest
import math
from area.area import area_quadrado, area_retangulo, area_triangulo, area_circulo 


@pytest.mark.parametrize("lado, expected", [
    (5, 25),
    (10, 100),
    (3, 9),
])
def test_area_quadrado(lado: Literal[5] | Literal[10] | Literal[3], expected: Literal[25] | Literal[100] | Literal[9]):
    assert area_quadrado(lado) == expected

@pytest.mark.parametrize("base, altura, expected", [
    (5, 4, 20),
    (10, 3, 30),
    (3, 6, 18),
])
def test_area_retangulo(base: Literal[5] | Literal[10] | Literal[3], altura: Literal[4] | Literal[3] | Literal[6], expected: Literal[20] | Literal[30] | Literal[18]):
    assert area_retangulo(base, altura) == expected


@pytest.mark.parametrize("base, altura, expected", [
    (6, 8, 24),
    (10, 5, 25),
    (4, 7, 14),
])
def test_area_triangulo(base: Literal[6] | Literal[10] | Literal[4], altura: Literal[8] | Literal[5] | Literal[7], expected: Literal[24] | Literal[25] | Literal[14]):
    assert area_triangulo(base, altura) == expected


@pytest.mark.parametrize("raio, expected", [
    (1, math.pi),
    (2, 4 * math.pi),
    (3, 9 * math.pi),
])
def test_area_circulo(raio: Literal[1] | Literal[2] | Literal[3], expected: float):
    assert math.isclose(area_circulo(raio), expected)