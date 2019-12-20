class Person:
    name = "Ivan"
    age = 29

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


igor = Student("Igor", 19)
igor.set("Igor", 23, 5)
print("Name:", igor.name, "Age:", igor.age, "Course:", igor.course)

vlad = Person("Vlad", 54)
vlad.set("Vlad", 57)
print(vlad.name + " " + str(vlad.age))

ivan = Person("Ivan", 27)
ivan.age = 45
print(ivan.name)
print(ivan.age)
