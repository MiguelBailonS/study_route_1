import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

def isSkipped():
    return True


#Fixture a crear:
#   * El nombre de la funcion debe ser igual al del paramaetro que quieres pasar por una funcion
#   * Para ser considerado fixture, debe ser decorado por pytest.fixture
@pytest.fixture
def username():
    return 'Miguel'#El valor que queramos asignar a dicho parametro

#Crear una prueba unitaria mediante una funcion
def test_username(username): #Para asignar un valor a este parametro, se lo puede hacer a traves de un fixture
    print(username)
    assert username == 'Miguel'

@pytest.fixture
def password():
    return '12345'
#Buena idea para utilizar features
def test_username_password(username,password):
    assert username == 'Miguel'
    assert password == password

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

    @pytest.mark.due_date 
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

    @pytest.mark.skip(reason = 'No se cumplen los requerimientos.')
    def test_skip(self):
        pass 

    @pytest.mark.skipif(isSkipped(),reason = 'No se cumplen los requerimientos.')
    def test_skipif(self):
        pass

    # Los Fixtures son funciones que se ejecutan antes de las pruebas unitarias
    # Los Fixtures proveen datos a las pruebas unitarias

#   Los fixtures:
#       * Son funciones que se ejecutan antes de las pruebas unitarias proveen datos a las pruebas unitarias   
#       * Cobran sentido cuando implementan pruebas unitarias a traves de funciones
#       * Se enfocan a trabajar en pruebas unitarias definidas mediante funciones