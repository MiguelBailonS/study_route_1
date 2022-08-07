import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

class TestTaskManager():

    def test_sample(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now() + timedelta(days = 1) #Modificacion de la prueba unitaria, para que pase.
        #Esto demuestra que un cambio en el código implementado, haría fallar otras pruebas.
        #En conclusión, el código falla por una validación que anteriormente no se tomo en cuenta.
        #Por lo tanto, se debe corregir en la implementación.
        task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)

        assert task.title == 'Investigacion'
        assert task.description == '10 de agosto'
        assert task.assigned_to == 'Miguel'
        assert task.due_date == due_date

    def test_due_date_error(self):

        #Debemos usar un contexto y el error que debe ser lanzado
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days = 1)
            task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)