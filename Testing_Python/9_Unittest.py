#En este bloque se utilizara Unittest <- Se encuentra en al biblioteca estandár de Python.

#Assert - Palabra reservada
#   Si la condicion se cumple -> El código se continua ejecutando normalmente
#   Si la condicion no se cumple -> Una excepción será lanzada.

if __name__ == '__main__':
    try:
        #assert 5 == 10, '5 is not equal to 10.' #Podemos enviar un mensaje a desplegar en caso que aparezca el Assertion Error.
        
        #Otra forma de hacer el 
        if not 5 == 10:
            raise AssertionError('5 is not equal to 10')
        
        #Los er

        print("Normal execution.")
    except AssertionError as error:
        #Con el try - except: No se mostrara el mensaje automatico de la linea 9.
        # EL mensaje de error se muestra implementando la linea 11 "AssertionError as error" e imprimiendolo en consola.
        print(error)

