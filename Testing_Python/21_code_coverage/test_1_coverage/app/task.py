from datetime import datetime

class DueDateError(Exception):
    pass

class Task():
    
    def __init__(self, title, description, assigned_to, due_date,status):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        if due_date < datetime.now():
            raise DueDateError('Fecha no valida')    
        self.due_date = due_date
        self.status = status

    # Se añaden nuevas funcionalidades
    def done(self):
        self.status = 'Done'

    def undone(self):
        self.status = 'Undone'