# Para este video hablaremos del DocString
# Mediante el DocString documentaremos el codigo. Funciones, clases, módulos y paquetes

# Veamos si una palabra es un palindromo

#DocString

"""
    Este comentario se lo conocera como DocString
        #Primer caracter en mayuscula.
    - Breve descripción del comportamiento del código. #Finalizar con punto
    
    Si el blque trabaja con diferentes objetos, hay que describirlos.
    Puntualmente, el/los parámetros y el objeto a retornar.

    Args:
        "Nombre del parámetro": Tipo de objeto

    Returns:
        Tipo de objeto

"""


def isPalindrome(sentence: str) -> bool:
    """ Determina si el string es palindromo.

    Args:
        sentence: string

    Returns:
        bool

    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

frase = "Anita lava la tina"
print(isPalindrome(frase))

frase = "No Es Palindromo"
print(isPalindrome(frase))
# Imprimir la documentación de la función. 
print(isPalindrome.__doc__)

#Función help(). Recibe como argumento la función de la que queremos conocer su documentación.
help(isPalindrome)

# Para documentar:  Funciones, clases, modulos, paquetes, etc. utilizaremos DocString.