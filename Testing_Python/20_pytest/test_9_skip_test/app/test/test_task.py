import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

def isSkipped():
    return True

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

    # Se utilizaran dos nuevas marcas para saltar pruebas:
    #   * Skip
    #   * SkipIf

    @pytest.mark.skip(reason = 'No se cumplen los requerimientos.')
    def test_skip(self):
        pass 

    # Se debe ingresar un bloque de codigo o statement
    @pytest.mark.skipif(isSkipped(),reason = 'No se cumplen los requerimientos.')
    def test_skipif(self):
        pass