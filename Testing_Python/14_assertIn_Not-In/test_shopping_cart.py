import unittest
from product import Product

#importamos la clase
from shopping_cart import shoppingCart

# Utilizaremos dos nuevos métodos de la clase unittest
# assertIn - assertNotIn
# Nos permite conocer si el objeto se encuentra o no dentro de una coleccion
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.name = 'iFon'
        self.price = 123.45
        self.smartphone = Product(self.name,self.price)
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
        self.assertTrue(self.shopping_cart_1.empty(),"Not empty.") 

    def test_sCart_notEmpty(self):
        self.assertTrue(self.shopping_cart_2.hasProducts(),"It doesnt have products")
        self.assertFalse(self.shopping_cart_1.hasProducts(),"It has products.")
    
    def test_product_in_sCart(self):
        #Si el objeto no se encuentra dentro de la coleccion, se lanzara una excepcion.
        self.assertIn(self.smartphone,self.shopping_cart_2.products)

        products_new = Product("Caja",10)
        self.shopping_cart_2.add_product(products_new)

        self.assertIn(products_new,self.shopping_cart_2.products)
    

    def test_product_not_in_sCar(self):
        #Eliminamos el producto del carrito de compras
        self.shopping_cart_2.removeProduct(self.smartphone)
        #Nos aseguramos si sirve el método, para saber si fue removido de la colección
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)


if __name__ == '__main__':
    unittest.main()
