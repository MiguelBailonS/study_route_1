# Se estructurará los módulos dentro del paquete "Entity"

from entities import Product
from entities import shoppingCart

# Vamos a observar el coverage con unittest.
# Para ello, se ejecutara el siguiente comando en la consola:
#   * coverage run -m unittest discover # Discover permite ejecutar todas las pruebas unitarias de manera recursiva.
# Se ha creado nuevamente el archivo ".coverage"
#   * coverage report
# La mayoria de archivos se han ejecutado con totalidad
#   * coverage report -m #Para concoer que lineas no se estan ejecutando

# Hacemos un refactor para aumentar el coverage de las pruebas unitarias
# Para generar nuevamente un reporte, ejecutamos:
#   * coverage run -m unittest discover
# Observamos nuevamente el archivo ".coverage" y vemos que el cover de las pruebas ha aumentado.