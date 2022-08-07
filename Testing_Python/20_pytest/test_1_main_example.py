#Para la ejecución de las pruebas unitarias se llama al comando "pytest". (Dentro del ambiente virtual)

# El comando ejecutara todas las pruebas de todos los archivos que empiecen con el prefijo "test_" en toda la ruta.
# Para conocer mas informacion, se añade la bandera "-v"
import pytest

#Se puede implementar pruebas unitarias mediante funciones.

#Las funciones deben incluir "test_"
def test_sample():
    # Para las pruebas, debemos utilizar assert.
    assert 10 == 10

def test_error_sample():
    assert 11 == 10, 'No paso.' #Ejecuta un error al ejecutar el comando "pytest"
