class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name}({self.age})"

#Object 
p1 = Person("Zeenath", 22)
print(p1)