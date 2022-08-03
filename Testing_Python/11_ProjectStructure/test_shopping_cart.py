#En este archivo se definiran las pruebas unitarias

import unittest
from product import Product

#Se realiza el test de la creacion de una instancia/objeto de clase Product 
class TestShoppingCart(unittest.TestCase):
    
    def test_product_object(self):
        name = "apple"
        price = 0.50
        product = Product(name,price)
        # Si un assertion llega a fallar, muestrta un assertionError
        self.assertEqual(product.name,name)
        self.assertEqual(product.price,price)
        # Se puede añadir mensajes
        self.assertEqual(product.price,0, "El precio no es igual")


if __name__ == '__main__':
    unittest.main()
# Cada punto en la consola, demuestra una prueba unitaria que ha pasado