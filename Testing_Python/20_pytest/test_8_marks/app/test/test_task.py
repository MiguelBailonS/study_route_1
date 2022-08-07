import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

class TestTaskManager():

    def test_sample(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days = 1) 
        task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)

        assert task.title == 'Investigacion'
        assert task.description == '10 de agosto'
        assert task.assigned_to == 'Miguel'
        assert task.due_date == due_date

#   Para ejecutar pruebas unitarias con marcas utilizamos la bandera "-m"
#   Ejemplo:
#       * pytest app/test -m due_date
#   Sin embargo, genera un warning.
#   Para solucionar el warning se crea un archivo:
#       * pytest.ini
#           - Se crean las marcas dentro del archivo: "due_date"
#           - Se registran las marcas


#   Notas:
#       * Una prueba puede poseer multiples marcas
#       * Una marca puede existir en multiples metodos
    @pytest.mark.due_date #Le podemos asignar marcas a las pruebas unitarias
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days = 1)
            task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days = 1) 
        task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)
        assert task.due_date > datetime.now()