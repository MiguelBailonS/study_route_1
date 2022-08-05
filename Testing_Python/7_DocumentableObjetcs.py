"""Este es el DocString del módulo main.
"""

#La linea 1 es la documentacion del módulo
#import main  #Para usar el import main, el archivo ".py" debe llamarse con main.

#Objetos documentables módulo, clase y método.

class User:
    #Documentar clase
    """Permite representar un usuario.
    """
    
    def __init__ (self, userName, password) -> None:
        #Documentar método
        """Permite crear la instancia de una clase User.

        Args:
            userName (_type_): Nombre de usuario
            password (_type_): Contraseña del usuario
        """
#print(main.__doc__)
print(User.__doc__)
print(User.__init__.__doc__)