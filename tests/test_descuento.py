import pytest
from descuento import descuento

def test_descuento_caso_correcto():
    assert descuento(100, 10) == 95.0

def test_descuento_caso_limite():
    assert descuento(250, 100) == 0.0

def test_descuento_caso_error_porcentaje_invalido():
    with pytest.raises(ValueError):
        descuento(100, 120)