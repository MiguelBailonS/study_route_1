#En Python, no hay un mecanismo que te aseguren los niveles de acceso a pesar de ser marcada como privada o protegida

# La convención es que:
# Si el nombre de la propiedad empieza con "_", es una propiedad protegida
# La convención de Python, se mantiene de esta manera.


class User: 
    #Propiedad pública
    name = ""
    #propiedad protegido
    _lastName = ""
    def __init__(self,name):
        #Propiedad pública
        self.name = name 
        #Propiedad protegida
        self._lastName = ""

    
    def wave(self, message):
        print(message,self.name)


class Employee(User): 
    #Propiedad privada
    __wage = 0
    def modifyWage(self, wage):
        self.__wage = wage
    
    def seeWage(self):
        print("El salario es: ",self.__wage)

    def wave(self):
        super().wave("Método padre")
        print("Hola mi salario es ", self.__wage, "y mi nombre es:", self.name)

employee_1 = Employee("Miguel") 
#Imposibilidad de acceder a ella a traves de la instancia ni desde subclases.
#print(employee_1.__wage) #Se generá un error

#A pesar de eso, aun se puede acceder a la propiedad, pero de una manera distinta:
print(employee_1._Employee__wage)

employee_1.modifyWage(100)
employee_1.seeWage()
employee_1.wave()

#Crearemos una clase que herede de la clase "Employee" y trataremos de acceder a la propiedad "wage"

class Developer(Employee):
    pass

developer_1 = Developer("Dev Miguel")
#print(developer_1.__wage) #Esta linea, genera un error