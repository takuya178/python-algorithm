class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self) -> str:
        return self.firstName + ' ' + self.lastName

    def getInitial(self) -> str:
        return self.firstName[0] + '.' + self.lastName[0]

mike = Person("Michael", "Johnson")
print(mike.getFullName())
print(mike.getInitial())

carly = Person("Carly", "Angelo")
print(carly.getFullName())
print(carly.getInitial())

jessie = Person("Jessie", "Raelynn")
print(jessie.getFullName())
print(jessie.getInitial())


class Dog:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def bark(self) -> str:
        if self.size >= 50:
            return 'Wooof! Woof!'
        elif self.size >= 20:
            return 'Ruff! Ruff!'
        else:
            return 'Yip! Yip!'

    def calcHumanAge(self) -> int:
        return 12 + (self.age - 1) * 7