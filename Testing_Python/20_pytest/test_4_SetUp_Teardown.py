import ssl
from this import d
import pytest

#SetUp y Teardown en Pytest

# Para que pytest imprima los mensajes del stdout, utilizamos la bandera "-s"

#   * pytest test_4_main.py -v -s
class TestExample():
    # Metodo setsup se ejecuta antes de cada prueba.
    def setup_method(self): # Funciona unicamento dentro de los metodos de clase
        print(">>>Setup method")
        self.numero_uno = 10
        self.numero_dos = 10

    # Metodo teardown se ejecuta despues de cada prueba.
    def teardown_method(self): # Funciona unicamento dentro de los metodos de clase
        print(">>>Teardown method")

    @classmethod
    def setup_class(cls):
        print(">>>Se ejecuta antes de todas las pruebas.")

    @classmethod
    def teardown_class(cls):
        print(">>>Se ejecuta despues de todas las pruebas.")

    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 20, 'Suma incorrecta.'

    def test_resta_dos_numeros(self):
        assert self.numero_uno - self.numero_dos == 0, 'Resta incorrecta.'


class TestExample2():

    def test_multiplicar_dos_numeros(self):
        assert 10 * 1 == 10,'Multiplicacion incorrecta'