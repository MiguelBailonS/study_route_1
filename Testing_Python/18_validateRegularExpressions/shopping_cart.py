from product import Product

class shoppingCart:

    def __init__(self) -> None:
       self.__products: List[Product] = []

    @property
    def products(self):
        return self.__products.copy()


    def empty(self) -> bool:
        return len(self.__products) == 0

    def hasProducts(self) -> bool:
        return not self.empty()

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def removeProduct(self, product:Product) -> None:
        self.__products.remove(product)

    @property
    def total(self) -> float:
        return sum( [ (product.price - product.discount) for product in self.__products] )