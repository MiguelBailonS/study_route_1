"""Este es el DocString del módulo main.
"""
import main 

#Documentar módulo, clase y método.

class User:
    """Permite representar un usuario.
    """
    
    def __init__ (self, userName, password) -> None:
        """Permite crear la instancia de una clase User.

        Args:
            userName (_type_): Nombre de usuario
            password (_type_): Contraseña del usuario
        """
print(main.__doc__)
print(User.__doc__)
print(User.__init__.__doc__)