#Incluir libreria de Unittest para hacer pruebas unitarias
import unittest

#Se recomienda iniciar los nombres de las clases de prueba con "Test"
class TestExample(unittest.TestCase):

    # Los nombres de todos los métodos para pruebas unitarias deben empezar con:
    # "test_"
    def test_suma_numeros(self):
        number1 = 10
        number2 = 20

        result = number1 + number2
        # La funcionn AssertEqual se encuentra en la clase "TestCase"
        #AssertEqual - Compara que dos objetos tengan el mismo valor
        self.assertEqual(result,30) # Similar a "assert result == 30"


    def test_restar_numeros(self):
        number1 = 10
        number2 = 20

        result = number1 - number2
        self.assertEqual(result,-10)

        

if __name__ == '__main__':
   unittest.main() #Ejecutara todos los métodos que empiecen con "test_"

   #Si se quiere conocer mas informacion de las pruebas se añade la bandera "-v" al ejecutar el script de Python