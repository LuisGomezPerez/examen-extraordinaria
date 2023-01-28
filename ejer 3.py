import string, random
import pytest
from main import armaduras, experimentacion

def test_experimentacion():
    n = 10
    lista_armaduras = experimentacion(n)
    assert len(lista_armaduras) == n
    for i in lista_armaduras:
        assert isinstance(i, armaduras)


def test_nombre_armaduras_valido():
    nombres_armaduras = [armaduras.nombre for armaduras in experimentacion(5)]
    for nombre in nombres_armaduras:
        assert nombre[2] == '-'
        assert nombre[:2].isalpha() and nombre[:2].isupper()
        assert nombre[3:].isnumeric()
        assert len(nombre) == 7
