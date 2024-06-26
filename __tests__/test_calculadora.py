from typing import Literal
import pytest
from area.calculadora.calculadora import somar_dois_numeros,subtrair_dois_numeros,multiplicar_dois_numeros,dividir_dois_numeros
from utils.utils import ler_csv     

def test_somar_dois_numeros():
    num1 = 5 
    num2 = 7
    resultado_esperado = 12 

    resultado_obtido = somar_dois_numeros(num1,num2) 

    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    num1 = 10 
    num2 = 6 
    resultado_esperado = 4

    resultado_obtido = subtrair_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

    
def test_multiplicar_dois_numeros():
    num1 = 3 
    num2 = 9 
    resultado_esperado = 27

    resultado_obtido = multiplicar_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    num1 = 64
    num2 = 4
    resultado_esperado = 16

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido



@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [
                            (5,7,12),
                            (0,8,8),
                            (10, -15, -5),
                            (6, 0.75, 6.75)  
                         ]
                        )

def test_somar_dois_numeros_lista(num1: Literal[5] | Literal[0] | Literal[10] | Literal[6], num2: float | Literal[7] | Literal[8] | Literal[-15], resultado_esperado: float | Literal[12] | Literal[8] | Literal[-5]):
 

    resultado_obtido = somar_dois_numeros(num1,num2) 

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_somar.csv') 
                         )

def test_somar_dois_numeros_lista_csv(num1: list | None, num2: list | None, resultado_esperado: list | None):
 

    resultado_obtido = somar_dois_numeros(float(num1),float(num2)) 

    assert float(resultado_esperado) == resultado_obtido

   
def test_dividir_por_zero():
    num1 = 64
    num2 = 0
    resultado_esperado = "Não é possível dividir por zero"

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido