# Uso del DocTest
# Probar el correcto funcionamiento de nuestro código mediante - DocTest

# Para poder realizar la prueba con DocTest, simulamos en la sección del DocString como si estuvieramos en consola.
# Para ejecutar setencias de Python, se escribe ">>> "
# En la linea siguiente, se escribe el resultado esperado.

# Comando de ejecución: python -m doctest "nombre_del_archivo.py" 
# Si el resultado es el esperado, no imprimira nada por consola.
# Si se obtiene una falla en el test, se mostrará una excepción

# Si se quieren observar los resultados, se añade la bandera "-v"
# Comando de ejecución: python -m doctest "nombre_del_archivo.py" -v

# Se recomienda no añadir más de 3 pruebas en el DocTest


# Usando DocString en conjunto con DocTest, podemos testear la función.
def isPalindrome(sentence: str) -> bool:
    """Determinar si la palabra/frase es palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.

    Examples:
        >>> isPalindrome("Anita lava la tina")
        True

        >>> isPalindrome("Hola")
        False

        >>> frase = "Oso"
        >>> isPalindrome(frase)
        True
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

frase = "Anita lava la tina"
print(isPalindrome(frase))
