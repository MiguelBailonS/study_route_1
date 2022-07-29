# Para conservar la funcionalidad del método, y solo extenderlo en la clase hija, se usa la función "super"
#Funcion super -> Retorna una instancia de la clase padre a través de la cual se pueden llamar métodos de la clase padre.

class User: 
    def __init__(self,name):
        self.name = name
    
    def wave(self, message):
        print(message,self.name)


class Employee(User): 
    wage = 0
    def modifyWage(self, wage):
        self.wage = wage
    
    def seeWage(self):
        print("El salario es: ",self.wage)

    def wave(self):
        #Ejecutaremos lo que habia en la clase padre. Y le agregaramos funcionalidades desde la subclase.
        super().wave("Método padre")
        #Funcionalidad del hijo
        print("Hola mi salario es ", self.wage, "y mi nombre es:", self.name)

employee_1 = Employee("Miguel") 
employee_1.modifyWage(1000)
employee_1.seeWage()
employee_1.wave()


#Veamos otro ejemplo

class Page:
    footPage = ""
    def printFootPage(self):
        print(self.footPage)
        
class LegalPage(Page):
    def printFootPage(self):
        print("Reserved Rights")
        super().printFootPage()

page = LegalPage()
page.footPage = "End"
page.printFootPage()

