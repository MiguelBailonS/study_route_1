
"""
    Métodos: Son funciones comunes que le pertenecen a un objeto.

    Funciones comunes de un método:
        * Alterar o modificar una propiedad
        * Retornar el valor de una propiedad
        * Realizar calculos u operaciones con las propiedades de un objeto
"""
class User:
    name = "default"

    #Para crear el método se utiliza la palabra reservada "def"
    #Se le asigna el nombre del método
    #En los parametros del método, siempre se empieza con "self" // Por convencion de la comunidad Python
    #   "Self" -> Hace referencia al objeto.
    def wave(self):
        print("Hola, mi nombre es ", self.name)

    def custom_wave(self,message):
        print(message,self.name)

    #Veamos el llamado a un método con paramatreos

#Creamos la instancia del objeto a partir de la clase User
user_obj = User()
user_obj.name = "Miguel"
#Para llamar al método creado en la clase, se utiliza el punto "."
#Como la función "wave" solo tiene como parámetro "self", en el llamado al método, este parámetro es omitido.
user_obj.wave()

#Veamos como seria una función con dos parámetros: "self" y "message"
user_obj.custom_wave("Este mensaje es personalizado, mi nombre es: ")
