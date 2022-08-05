import unittest
from product import Product

#importamos la clase
from shopping_cart import shoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.name = 'iFon'
        self.price = 123.45
        self.smartphone = Product(self.name,self.price)
        #Instanciamos un objeto de la clase shoppingCart
        self.shopping_cart_1 = shoppingCart()
        self.shopping_cart_2 = shoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

        print("Setup: Se ejectura antes de cada una de las pruebas")

    def tearDown(self):
        print("tearDown: Se ejectura despues de cada una de las pruebas")

    @classmethod
    def setUpClass(cls):
        print("setUpClass: antes de todas lsa pruebas.")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass: Despues de TODAS las clases.")

    def test_product_object(self):
        name = "apple"
        price = 0.50
        product = Product(name,price)
        self.assertEqual(product.name,name)
        self.assertEqual(product.price,price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name,self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price,self.price)

    def test_sCart_empty(self):
        #El carrito esta vacio
        #assertTrue devuelve OK, si el argumento es True.
        # Caso contrario hace un Raise de AssertionError
        self.assertTrue(self.shopping_cart_1.empty(),"Not empty.") 

    def test_sCart_notEmpty(self):
        self.assertTrue(self.shopping_cart_2.hasProducts(),"It doesnt have products")
        #Funcion similar que assert True que evalua si el argumento a evaluar es falso.
        self.assertFalse(self.shopping_cart_1.hasProducts(),"It has products.")
    
if __name__ == '__main__':
    unittest.main()
