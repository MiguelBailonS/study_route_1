from product import Product

class shoppingCart:

    def __init__(self) -> None:
       self.__products: List[Product] = []

    #Método que devuelve una copia de la lista de productos. 
    # Asi evitamos que objetos externos añadan o eliminen elementos
    
    #El método se convi erte en atributo con "propierty"
    @property
    def products(self):
        return self.__products.copy()


    def empty(self) -> bool:
        return len(self.__products) == 0

    def hasProducts(self) -> bool:
        return not self.empty()

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    # Método para remover un producto de la lista
    # TODO Asegurarse primero que el objeto si exista en la lista(?)
    def removeProduct(self, product:Product) -> None:
        self.__products.remove(product)