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