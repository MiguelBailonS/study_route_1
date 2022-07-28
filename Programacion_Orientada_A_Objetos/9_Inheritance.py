

#User es la clase más general
class User:
 
    def __init__(self,name):
        self.name = name
    
    def wave(self, message):
        print(message, self.name)


#Employee va a heredar de la clase User
#Para heredar de una clase, se escribe dentro del parantesis la clase padre/base.
#class __nombreDeClase__(__ClaseAHeredar1__,_ClaseAHeredar2__,...)
class Employee(User):
    pass

employee_1 = Employee()