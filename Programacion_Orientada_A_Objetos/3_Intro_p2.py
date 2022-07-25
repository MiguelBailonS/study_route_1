
"""
    Cualquier instancia de la clase User tendra las siguientes propiedades
        * name
"""
class User:
    name = "default"
    pass

print("Atributos de la clase ´User´",User.__dict__)

#user_obj es un nuevo objeto de la clase usuario
user_obj = User()
#Para acceder a las propiedades de las clases se utiliza un punto "-"
print("Valor de la propiedad ´name´ en user_obj: ",user_obj.name)


#Se crea una nueva propiedad al objeto "user_obj" por fuera de la declaración de la clase
#NO ES RECOMENDABLE
user_obj.email = "miguel.bailon@course.com"
print("Valor de la nueva propiedad ´email´ en user_obj: ",user_obj.email)

#Para modificar el valor de la propiedad de user_obj puedo hacer lo siguiente:
user_obj.name = "Miguel"
print("Nuevo valor de la propiedad ´name´ en user_obj: ",user_obj.name)


#Cada instancia de la clase, posee estados distintos.
#La modificacion de un objeto, no afecta al otro

user2_obj = User()
user2_obj.name = "Alejandro"
#Se observan que el valor del user_obj no han cambiado.
print("Valor de la propiedad ´name´ en user_obj: ",user_obj.name)
print("Valor de la propiedad ´name´ en user2_obj: ",user2_obj.name)
