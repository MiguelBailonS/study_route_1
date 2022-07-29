

#User es la clase más general
class User:
 
    def __init__(self,name):
        self.name = name
    
    def wave(self, message):
        print(message,self.name)


#Employee va a heredar de la clase User
#Para heredar de una clase, se escribe dentro del parantesis la clase padre/base.
#class __nombreDeClase__(__ClaseAHeredar1__,_ClaseAHeredar2__,...)
class Employee(User): #La clase User es la clase padre de Employee. #La clase Employee es hijo/hereda de la clase padre User.
    wage = 0
    def modifyWage(self, wage):
        self.wage = wage
    
    def seeWage(self):
        print("El salario es: ",self.wage)

    def wave(self):
        print("Hola mi salario es ", self.wage, "y mi nombre es:", self.name)

employee_1 = Employee("Miguel") # A pesar de no definir el método constructor en Employee. Hereda el constructor de User, por lo que
                                # requiere el parametro "name"

#employee_1.wave("Hola ")
employee_1.modifyWage(1000)
employee_1.seeWage()
#Estamos sobreescribiendo el método wave para la clase employee. 
# Ahora, hace referencia al método de la clase en la que estamos instanciando y no al método que se encuentra en la clase padre User.
employee_1.wave()

#Concepto de multiples herencias:
# Una sola clase puede heredar de muchas clases.