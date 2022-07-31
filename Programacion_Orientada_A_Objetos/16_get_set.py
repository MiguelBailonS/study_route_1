# Métodos accesores "Get" y "Set"
#Encapsular una propiedad que antes era pública sin modificar un codigo que ya estaba escrito.
class User: 
    #Creamos una nueva propiedad llamada "Age"
    __age = 0
    name = ""
    _lastName = ""
    
    #Usaremos el decorador: "property" para crear los modificadores de la propiedad privada "age"
    @property #Definimos el metodo getter. 
    def age(self): #Para que la solucion sustituya el valor de la propiedad edad, se le otorga el nombre al método
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

    def __init__(self,name):
        self.name = name 
        self._lastName = ""

    
    def wave(self, message):
        print(message,self.name)


class Employee(User): 
    __wage = 0

    """
    Métodos públicos para obtener y modificar el valor de la propiedad privada "wage"
        * Obtener -> seeWage()
        * Cambiar -> modifyWage(wage)

    Se pueden considerar como métodos accesores
    """
    def modifyWage(self, wage): #Método "Set" de cambiar salario
        self.__wage = wage
    
    def seeWage(self): #Método "Get" de obtener salario
        print("El salario es: ",self.__wage)



    def wave(self):
        super().wave("Método padre")
        print("Hola mi salario es ", self.__wage, "y mi nombre es:", self.name)

employee_1 = Employee("Miguel") 
print(employee_1.age) #Getter
employee_1.age = 26
print(employee_1.age) #Cabe destacar que no se utiliza el parentesis para el método getter debido al decorador @property


# print(employee_1._Employee__wage)

#employee_1.modifyWage(100)
#employee_1.seeWage()
#employee_1.wave()

