#En alguno como Java, hay clases abstractas
#Ruby: ofrece otros elementos
#En Python, no hay interfaces, pero si hay clases abstractas

 #Veamos un ejemplo sencillo de abstraccion:

class queue:
    data = []

    def add(self, key, value):
        self.data[len(self.data)-1] = value

    def getNext(self,key):
        return self.data[0]


class Hash():
    data = {}
    def add(self,key,value):
        self.data[key] = value

    def getNext(self,key):
        return self.data[key]


#Esta clase esta creada con un problema: No aplica abstraccion al momento de cambiar el tipo "client" de Hash a Diccionario y viceversa.
# Lo que generaria un error
class queueBank():

    clients = {} #Hashmap o Diccionario
    
    def addUser(self, number, user):
        #Implementacion
        self.clients[number] = user

    def nextUser(self, number):
        #Implementacion
        return self.clients[number]

#Solucion si usara Hash
class queueBank_Hash():
    clients = Hash()

    def addUser(self, number, user):
        self.clients.add(number,user)

    def nextUser(self, number):
        return self.clients.getNext(number)

#Solucion si usara queue
class queueBank_queue():
    clients = queue()

    def addUser(self, number, user):
        self.clients.add(number,user)

    def nextUser(self, number):
        return self.clients.getNext(number)

# IMPORTANTE
# Se puede observar que los metodos addUser y nextUser en las clases queueBank_hash y queueBank_queue
# Realmente no han cambiado nada, esto es debido a la abstraccion
# Además, porquie el problema se atacó de lo más general, a lo más especifico.
# Lo más general: "Añadir elementos a un Hash/diccionario" y "Obtener el siguiente elemento del Hash/Diccionario"
# Lo mas especifico: Almacenar clients y obtener el siguiente cliente en la fila o añadir uno.