import pytest

#La clase de pruebas debe contenter obligatoriamente el prefijo "Test"
class TestExample():
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Suma incorrecta.'

    def test_resta_dos_numeros(self):
        assert 10 - 10 == 0, 'Resta incorrecta.'

    