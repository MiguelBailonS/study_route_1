# Se estructurará los módulos dentro del paquete "Entity"

from entities import Product
from entities import shoppingCart

# Con Coverage, se pueden presentar los reportes de cover de una forma mas visual, mediante HTML
# Se genera el archivo '.coverage'

# En este caso: con unittest

# A partir del resumen, se genera el maquetado HTML
#   * 'covergae html'

# Mediante este archivo, generaremos el reporte de manera mas visual.
# Como son archivos html, se recomienda hacerlo a traves de un navegador web.

# Levantamos un pequeño servidor web
# python -m http.server
# Ingresamos a localhost:8000
# Ingresamos a la carpeta htmlcov
# Se indican que todos los archivos generan un reporte del 100% ( o casi todos)

# Podemos ver cuales son las lineas que se han ejecutado, mediante un navegador web
