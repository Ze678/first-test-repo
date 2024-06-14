#__init__ function - to assign values

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

        
#new Object(p1) for assigning the values
p1 = Person("Zeenath", 22)
print(p1.name)
print(p1.age)