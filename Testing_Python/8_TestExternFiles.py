#DocTest no es un framework de Testing. -> Carece de ciertas herramientas para realizar las pruebas unitarias.

#Se pueden hacer los test dentro de DocString, pero esta orientado a la documentación.

#Se puede crear un archivo independiente para realizar las pruebas unitarias.

#Se moveran los test a otros archivos.
#Para poder hacer esto, el archivo debe empezar con "test_".

# Para poder hacer la prueba, se utiliza en consola el siguinete comando: "python -m doctest test_class_8.txt"

def isPalindrome(sentence: str) -> bool:
    """Determinar si la palabra/frase es palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

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
        self.username = userName
        self.password = password
#print(main.__doc__)
print(User.__doc__)
print(User.__init__.__doc__)