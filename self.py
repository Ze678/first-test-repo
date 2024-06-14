class Person:
    def __init__(silly, name, age):
        silly.name = name
        silly.age = age

    def myFunc(abc):
        print("I'm "+ abc.name)

p1 = Person("Zeeanth", 21)
p1.age = 22
p1.myFunc()
del p1
p1.myFunc()
