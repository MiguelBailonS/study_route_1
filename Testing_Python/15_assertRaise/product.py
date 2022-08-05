# Crearemos nuestro propio error

#Para ser considerada un error, debe heredad de Exception
class productDiscountError(Exception):
    pass

class Product:
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        if(discount > price):
            #De esta manera, levantamos nuestro propio error
            raise productDiscountError("El descuento no puede ser mayor al precio del producto.")
        self.discount = discount

    