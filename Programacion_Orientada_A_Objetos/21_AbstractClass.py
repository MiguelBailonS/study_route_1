#Diseño de nuestras clases y no la implementacion de la misma
#Diseñamos el esqueleto de la clase y son las clases hijas quienes se dedican a la implementación

#Para crear clases abstractas para  el diseño del esqueleto, necesitas importar 
#   * Modulo
#       - abc
#           / ABC               <- clase
#           / abstractmethod    <- decorador
# ejemplo:
# from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


#Definamos una clase abstracta que debe heredar de ABC. - Cualquier clase a ser abstracta, debe heredar de ABC
class abstractStructure(ABC):
    #Los métodos de una clase abstracta se caracteriza por no tener implementación
    @abstractmethod
    def getNext():
        # No hay implementacion
        pass

    @abstractmethod
    def add():
        # No hay implementacion     
        pass

#Si una clase hereda de una clase abstracta
#   * Se debe implementar obligatoriamente todos los metodos abstractos prototipados en la clase abstracta.
class Hash(abstractStructure):
    data = {}
    def add(self,key,value):
        self.data[key] = value

    def getNext(self,key):
        return self.data[key]

class queueBank_generic():
    
    def __init__(self,type):
        if not isinstance(type,abstractStructure):
            raise ValueError("Type is not from an abstract Structure")
        self.clients = type

    def addUser(self, number, user):
        self.clients.add(number,user)

    def nextUser(self, number):
        return self.clients.getNext(number)


queueBank = queueBank_generic(Hash())

#queueBank_2 = queueBank_generic([]) - Esta linea retorna un error ya que "[]" no es de instancia abstractStructure