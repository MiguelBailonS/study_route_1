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
# Podemos modificar ligeramente los fixtures para simular que estamos trabajando con los metodos Setup y dearDown
# Si hacemos pruebas unitarias unicamente por funciones, podemos utilizar los fixtures como Setup y tearDown
@pytest.fixture
def username():
    print('>>> Antes de la prueba')
    yield 'Miguel' #Yield retornara el valor cada que se ejecuta
    print('>>> Despues de la prueba.')

def test_username(username):
    print(username)
    assert username == 'Miguel'

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

