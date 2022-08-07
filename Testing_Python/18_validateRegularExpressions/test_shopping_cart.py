import unittest
from product import Product
from shopping_cart import shoppingCart
from product import productDiscountError


def is_available_to_skip():
    return True

def is_avaiable_to_skip_unless():
    return False

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.name = 'iFon'
        self.price = 123.45
        self.smartphone = Product(self.name,self.price)
        self.shopping_cart_1 = shoppingCart()
        self.shopping_cart_2 = shoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)
        #print("Setup: Se ejectura antes de cada una de las pruebas")

    def tearDown(self):
        #print("tearDown: Se ejectura despues de cada una de las pruebas")
        pass

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
        self.assertIn(self.smartphone,self.shopping_cart_2.products)

        products_new = Product("Caja",10)
        self.shopping_cart_2.add_product(products_new)

        self.assertIn(products_new,self.shopping_cart_2.products)
    

    def test_product_not_in_sCar(self):
        self.shopping_cart_2.removeProduct(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_discount(self):
        with self.assertRaises(productDiscountError): 
            product_disc = Product("Pavo",10,15)

    def test_total_shopC(self):
        self.shopping_cart_1.add_product(Product(name ='book', price = 15.0))
        self.shopping_cart_1.add_product(Product(name = 'camera', price = 600, discount = 100))

        self.assertGreater(self.shopping_cart_1.total,0) 
        self.assertLess(self.shopping_cart_1.total,1000) 
        self.assertEqual(self.shopping_cart_1.total, 515) 

    def test_empty_shopC(self):
        self.assertEqual(self.shopping_cart_1.total,0)

    @unittest.skip('No estan los requerimientos necesarios')
    def test_skip_sample(self):
        self.assertEqual(1,1)

    @unittest.skipIf(is_available_to_skip(), 'Se saltara la prueba - SkipIf')
    def test_skip_if_sample(self):
        pass

    @unittest.skipUnless(is_avaiable_to_skip_unless(), 'Se saltara la prueba - SkipUnless')
    def test_skip_unless_sample(self):
        pass

    # Vamos a evaluar expresiones regulares.
    # Vmaos a condicionar que el codigo de nuestro producto sea el correcto.

    # Creamos la prueba

    def test_regular_expression_code(self):
        # De esta manera podemos buscar un substring que se encuentre dentro de otro

        # Para evaluar expresiones regulares se usa: "assertRegex"
        self.assertRegex(self.smartphone.code, self.smartphone.name) #Regex

if __name__ == '__main__':
    unittest.main()
