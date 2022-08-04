from product import Product

class shoppingCart:

    #Construyendo el proyecto con anotaciones
    def __init__(self) -> None:

#        self.__products = list() #Atributo Privado

        #Forma de crear la lista con anotaciones
        self.__products: List[Product] = []

#Implementar pruebas unitarias para estas funciones
    def empty(self) -> bool:
        return len(self.__products) == 0

    def hasProducts(self) -> bool:
        return not self.empty()

    #TODO Validar que el objeto a añadir es una instancia de la clase Product

    def add_product(self, product: Product) -> None:
        self.__products.append(product)