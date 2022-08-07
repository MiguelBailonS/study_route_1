import pytest

#Podemos ejecutar unicamente solo pruebas unicamente de cierta clase.


#   <Modulo><Clase><Metodo>
#   * pytest test_3_main.py::TestExample # Todos los metodos de una clase en especifico
#   * pytest test_3_main.py::TestExample::test_resta_dos_numeros #Método especifico de una clase
#
class TestExample():
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Suma incorrecta.'

    def test_resta_dos_numeros(self):
        assert 10 - 10 == 0, 'Resta incorrecta.'


class TestExample2():

    def test_multiplicar_dos_numeros(self):
        assert 10 * 1 == 10,'Multiplicacion incorrecta'