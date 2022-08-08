import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

def isSkipped():
    return True

"""
@pytest.fixture
def username():
    return 'Miguel'

def test_username(username): 
    print(username)
    assert username == 'Miguel'

@pytest.fixture
def password():
    return '12345'

def test_username_password(username,password):
    assert username == 'Miguel'
    assert password == password
"""
@pytest.fixture
def username():
    print('>>> Antes de la prueba')
    yield 'Miguel' 
    print('>>> Despues de la prueba.')

def test_username(username):
    print(username)
    assert username == 'Miguel'

class TestTaskManager():

    def test_sample(self):
        assert True

    # Vamos a parametrizar las pruebas.
    # Con la parametrización, podemos ejecutar distintas pruebas unitarias con valores dinamicos tal como se muestra a continuación.

    @pytest.mark.news
#    def test_new_task(self):
    @pytest.parametrize(
        'title, description, assigned_to,due_date', #Colocaremos todos los parametros para llevar a cabo la prueba en string
        #Se crea dentro de una lista, una n cantidad de tuplas. El test se ejecutara una vez por cada tupla dentro de l alista.
        [
            ('Title 1', 'Description', 'User 1', datetime.now() + timedelta(days=1)) #Se hara prueba de acuerdo a la cantidad de tuplas creadas
            ('Title 2', 'Description', 'User 2', datetime.now() + timedelta(days=2)) 
            ('Title 3', 'Description', 'User 3', datetime.now() + timedelta(days=3)) 
        ]
    )
    def test_new_task(self,title,description,assigned_to,due_date):
        due_date = datetime.now() + timedelta(days = 1) 
        task = Task(title, description, assigned_to, due_date)

        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
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

