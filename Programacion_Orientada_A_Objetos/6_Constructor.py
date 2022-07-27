# En los lenguajes de programación con el paradigma de programación orientada a objetos existe un método especial denominado
# Método constructor:
#   * Se ejecuta de manera automatica cuando se instancia un nuevo objeto de una clase.
#   * El método constructor tiene un nombre definido en el lenguajeç
#       - En Python: "__init__"

class User():
    name = ""
    #Método constructor 
    def __init__(self):
        pass

class User_with_args():
    name = ""
    #Método constructor con argumento
    def __init__(self, name):
        self.name = name

#Al crear un nuevo método, el método __init__ se ejecuta automaticamente.
#Cualquier propiedad requerida para que el objeto este inicializado correctamente, se debe pasar como argumento al instanciar el objeto.
user_obj = User()

#Método constructor con argumento requerido al instanciar un nuevo objeto de la clase User_with_args.
user_obj_2 = User_with_args("Miguel")
print("User with args:", user_obj_2.name)


