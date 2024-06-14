class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def myFunc(self):
        print("I'm "+self.name)

p1 = Person("Zeenath", 21)
p1.myFunc()