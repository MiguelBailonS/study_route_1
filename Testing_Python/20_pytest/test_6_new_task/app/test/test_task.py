import pytest

from app.task import Task
from datetime import datetime


class TestTaskManager():

    def test_sample(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now()
        task = Task('Investigacion', '10 de agosto', 'Miguel', due_date)

        assert task.title == 'Investigacion'
        assert task.description == '10 de agosto'
        assert task.assigned_to == 'Miguel'
        assert task.due_date == due_date
