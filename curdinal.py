class Animal:
    def __init__(self, species: str, weightKg: int, heightM: int, predator: bool):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator

    def domesticate(self):
        self.predator = False
        return self.predator

class Hunter:
    def __init__(self, name: str, weightKg: int, heighM: int, strength: int, cageCubicMeters: int):
        self.name = name
        self.weightKg = weightKg
        self.heighM = heighM
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters

    def strengthKg(self) -> int:
        return self.strength * self.weightKg

    def canCaptureAnimal(self, animal: Animal) -> bool:
        return self.strengthKg() >= animal.weightKg and self.cageCubicMeters >= animal.heightM and not animal.predator

    def attemptToDomesticate(self, animal: Animal) -> bool:
        if self.strengthKg() > animal.weightKg * 2:
            return animal.domesticate()

tiger = Animal("Tiger", 290, 2.6, True)
cow = Animal("Cow", 1134, 1.5, False)
snake = Animal("Snake", 100, 1.2, True)
cat = Animal("Cat", 10, 0.5, False)
hunternator = Hunter("Hunternator", 124.73, 1.85, 15, 3)
animals = [tiger, cow, snake, cat]

def capturedAnimals(hunternator: Hunter, animals: list):
    for i in range(len(animals)):
        if hunternator.canCaptureAnimal(animals[i]):
            print(animals[i].species)


def domesticateTheAnimals(hunternator: Hunter, animals: list) -> list:
    for i in range(len(animals)):
        hunternator.attemptToDomesticate(animals[i])
    return animals

capturedAnimals(hunternator, animals)

domesticateTheAnimals(hunternator, animals)
capturedAnimals(hunternator, animals)


import random

def chooseNFromBags2d(n, listOfBags):
    totalBags = len(listOfBags)
    chosenNumbers = []
    counter = 0
    while counter < n:
        currentBag = listOfBags[counter % totalBags]
        chosenNumbers.append(currentBag[random.randint(0, len(currentBag)-1)])
        counter+=1
    return chosenNumbers

luckyArrayOfBags = [[21,5,12,25],[100,88,354,643],[122,145,825,4],[228,674,777,77]]


class Student:
    def __init__(self, studentId: str, firstName: str, lastName: str, gradeLevel: int):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel

    def getStudentInfo(self) -> str:
        return f'{self.studentId}:{self.firstName} {self.lastName}({self.gradeLevel}gr)'

class Classroom:
    def __init__(self, students: list, courseName: str, teacher: str):
        self.students = students
        self.courseName = courseName
        self.teacher = teacher

    def getClassIdentity(self) -> str:
        return f'{self.courseName} managed by {self.teacher}'

    def getNumberOfStudents(self) -> int:
        return len(self.students)

def printHonorsStudents(schools: list) -> str:
    honorStudent = ''
    for i in range(len(schools)):
        for j in range(len(schools[i].students)):
            if student.gradeLevel > 10:
                honorStudent += f'{student.getStudentInfo()} from {school.teacher}s class'
    return honorStudent


def fibonacciNumberStack(n, arrayOutput):
    outputStack = []

    if n == 0:
        outputStack.append(0)
        arrayOutput.append(outputStack)
        return 0

    elif n == 1:
        outputStack.append(1)
        arrayOutput.append(outputStack)
        return 1

    answer1 = fibonacciNumberStack(n - 1, outputStack)
    answer2 = fibonacciNumberStack(n - 2, outputStack)

    # print(answer1)
    outputStack.append(answer1 + answer2)
    arrayOutput.append(outputStack)
    # print(arrayOutput)
    # print(outputStack)

    return answer1 + answer2


def flatten(multiarray):
    arr1d = []
    for value in multiarray:
        if isinstance(value, list):
            arr1d += flatten(value)
        else:
            arr1d.append(value)
    return arr1d


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    answer1 = fib(n-1)
    answer2 = fib(n-2)
    print(answer2)

    return answer1 + answer2

def maxAscilString(stringList: list) -> int:
    asciList = []
    asciNumber = 0
    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            asciNumber += ord(stringList[i][j])
        asciList.append(asciNumber)
        asciNumber = 0

    return asciList.index(max(asciList))

maxAscilString(["egvnPZgyCh","bridge","Fantastic"])


