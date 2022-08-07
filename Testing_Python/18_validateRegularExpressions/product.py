class productDiscountError(Exception):
    pass

class Product:
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        if(discount > price):
            raise productDiscountError("El descuento no puede ser mayor al precio del producto.")
        self.discount = discount

    #Este metodo va a simular la creacion de un código
    @property
    def code (self):
        return f'code-{self.name}'