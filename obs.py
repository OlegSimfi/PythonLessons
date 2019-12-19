class Person:
    name = "Ivan"
    age = 29

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1


igor = Student()
igor.set("Igor", 19)
print(igor.name)
print(igor.course)

vlad = Person()
vlad.set("Vlad", 54)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.age = 45
print(ivan.name)
print(ivan.age)
