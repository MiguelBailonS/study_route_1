#Lo primero que se hará es instalar la libreria "coverage"
# En el ambiente virtual se debe ejectuar:
#   * pip install coverage

# Vamos a conocer que porcentage del codigo se ejecuta, se realiza mediante las pruebas unitarias.

# Quiero ver que parte del codigo de la clase Task se ejecuta.

# En la consola se debe ejecutar el siguiente comando
#   * 'coverage run -m pytest app/test/test_task.py -v'

# UN archivo con extension ".coverage" se creara.
# Para observar el reporte de las pruebas, se ejecuta en consola:
#   * 'coverage report'

# Para conocer mas informacion del reporte, añadimos la bandera '-m'
# Aqui se incluiran las lineas que no fueron ejecutadas.

# Tener el coverage al 100%, significa que todo el código de ese archivo .py/modulo se ha ejecutado.

# Se añadieron nuevas funcionalidades: Los metodods "Done" y "Undone"
# Al correr nuevamente el coverage, se observará que el coverage del modulo task ha disminuido, pues no se ejecutan ciertas lineas.

# Taller: Crear las tareas dentro del task manager.