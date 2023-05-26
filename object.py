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

import math

class Animal:
    def __init__(
        self,
        name: str,
        weightKg: int,
        heightM: int,
        isPredator: bool,
        speedKph: int,
    ):
        self.name = name
        self.weighKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph

    activityMultiplier = 1.2

    def getBmi(self) -> int:
        return math.floor(round(self.weighKg / (self.heightM**2), 2) * 100) / 100

    def getDailyCalories(self) -> int:
        return math.floor(round(70 * (self.weighKg**0.75) * self.activityMultiplier, 2) * 100) / 100

    def isDangerous(self) -> bool:
        return True if self.isPredator or self.heightM >= 1.7 or self.speedKph >= 35 else False