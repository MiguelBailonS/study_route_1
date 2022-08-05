import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):
    # Introduccion a metodos Setup y Teardown
    # setUp y tearDown se ejecutan a nivel de métodos
    def setUp(self):
        #Aqui se puede inicializar los objetos para hacer uso de las pruebas unitarias
        self.name = 'iFon'
        self.price = 123.45
        self.smartphone = Product(self.name,self.price)
        print("Setup: Se ejectura antes de cada una de las pruebas")

    def tearDown(self):
        #Se puede reestablecer los objetos creados.
        
        print("tearDown: Se ejectura despues de cada una de las pruebas")

    #Los siguientes métodos, seran metodos de clases.
    #Se ejecutaran antes o despues de la ejecucion de TODAS las pruebas unitarias

    @classmethod
    def setUpClass(cls):
        #Un ejemplo de su uso: es establecer la coenxion con una base deew datos para TODAS las pruebas.
        print("setUpClass: antes de todas lsa pruebas.")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass: Despues de TODAS las clases.")

    def test_product_object(self):
        name = "apple"
        price = 0.50
        product = Product(name,price)
        # Si un assertion llega a fallar, muestrta un assertionError
        self.assertEqual(product.name,name)
        self.assertEqual(product.price,price)
        # Se puede añadir mensajes
        #self.assertEqual(product.price,0, "El precio no es igual")

    def test_product_name(self):
        self.assertEqual(self.smartphone.name,self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price,self.price)

if __name__ == '__main__':
    unittest.main()
