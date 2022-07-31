#Ejemplo sin polimorfismo

def returnMax(first_instance, second_instance):
    if isinstance(first_instance,int) and isinstance(second_instance,int):
        if first_instance > second_instance:
            return first_instance
        return second_instance
    
    if isinstance(first_instance,str) and isinstance(second_instance,str):
        words = [first_instance,second_instance]
        words.sort()
        return words[0]
    
    if isinstance(first_instance,list) and isinstance(second_instance,list):
        if len(first_instance) > len(second_instance):
            return first_instance
        return second_instance

print(returnMax(1,2))
print(returnMax("Miguel","Alejandro"))
print(returnMax([1,2,3],[2,3]))

#La solución que estamos viendo actualmente es ineficiente.

#<>
class Number_():
    value = 0
    def __init__(self,number):
        self.value = number

    def compare(self,number):
        if number.value > self.value:
            return number.value
        return self.value

class String_():
    value = ""
    def __init__(self,string):
        self.value = string
        
    def compare(self,string):
        words = [string.value,self.value]
        words.sort()
        return words[0]

class List_():
    value = []
    def __init__(self,list):
        self.value = list

    def compare(self,list):
        if len(list.value) > len(self.value):
            return list.value
        return self.list
#Los objetos toman la forma necesaria para retornar el mayor valor.
def returnMax_(first,second):
    #Los objetos toman la forma adecuada para que funcione.
    return first.compare(second)

print("Ejemplo de polimorfismo-")
number_one = Number_(10)
number_two = Number_(2)

print(number_one.compare(number_two))

string_one = String_("Miguel")
string_two = String_("Alejandro")
print(string_one.compare(string_two))

list_one = List_([1,2,3,4,5])
list_two = List_([1,2,3,4,5,6])
print(list_one.compare(list_two))
