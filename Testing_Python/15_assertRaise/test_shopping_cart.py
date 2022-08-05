import unittest
from product import Product
from shopping_cart import shoppingCart


#importamos la clase
from product import productDiscountError

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
        self.shopping_cart_2.removeProduct(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_discount(self):
        #Para usar el metodo assertRaise, obligatoriamente debe hacerlo bajo un contexto.

        #Se paso como argumento, la instacia del error esperado.
        with self.assertRaises(productDiscountError): #Exitosamente capturo el error.
            product_disc = Product("Pavo",10,15)

if __name__ == '__main__':
    unittest.main()
