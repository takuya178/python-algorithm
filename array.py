def getMaxIndex(arr: list):
    max_num = max(arr)
    results = []
    for i in range(len(arr)):
        if arr[i] == max_num:
            results.append(i)
    return max(results)

def sortByMaxMin(arr: int):
    sortList = []
    while len(arr) > 0:
        maxNumber = max(arr)
        minNumber = min(arr)
        if len(arr) == 1:
            sortList.append(maxNumber)
        else:
            sortList.append(maxNumber)
            sortList.append(minNumber)
        arr.remove(maxNumber)
        if len(arr) <= 1: break
        arr.remove(minNumber)

    return sortList

def addEveryOtherElement(intArr):

# リスト内の要素の足し合わせ
def addEveryOtherElement(intArr):
    addNumber = 0
    for i in range(len(intArr)):
        if i % 2 == 0:
            addNumber += intArr[i]
    return addNumber + intArr[0]

# 1つ飛ばしする方法
def addEveryOtherElement2(intArr):
    sumOfArr = 0
    for i in intArr[::2]:
        sumOfArr += i
    return sumOfArr

# 文字カウント
def charInBagOfWordsCount(bagOfWords: list, keyCharacter: int):
    count = 0
    for i in range(len(bagOfWords)):
        for j in range(len(bagOfWords[i])):
            if bagOfWords[i][j] == keyCharacter:
                count += 1
    return count


# 文字コード
import string

def createAscObj():
    obj = {}
    ascNum = 97
    for char in string.ascii_lowercase:
        obj[char] = ascNum
        ascNum += 1

    return obj

def isFirstStringLarger(s1: str, s2: str) -> bool:
    sumS1Number = 0
    sumS2Number = 0
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')
    for i in range(len(s1)):
        sumS1Number += createAscObj()[s1[i]]
    for i in range(len(s2)):
        sumS2Number += createAscObj()[s2[i]]

    return True if sumS1Number > sumS2Number else False



def isFirstStringLarger(s1,s2):
    return getAscii(s1) > getAscii(s2)

def getAscii(string):
    sumOfAscii = 0
    for char in string.lower():
        sumOfAscii += ord(char)
    return sumOfAscii

# 間のアルファベット
def createAlphabetList(firstAlphabet: str, secondAlphabet: str):
    alphabetList = []
    for char in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower())+1):
        alphabetList.append(chr(char))
    return alphabetList

def generateAlphabet(firstAlphabet: str, secondAlphabet: str):
    return createAlphabetList(firstAlphabet, secondAlphabet) if ord(firstAlphabet.lower()) <= ord(secondAlphabet.lower()) else createAlphabetList(secondAlphabet, firstAlphabet)

def generateAlphabet(firstAlphabet,secondAlphabet):
    first = firstAlphabet.lower()
    second = secondAlphabet.lower()

    smaller = ord(second) if ord(first) > ord(second) else ord(first)
    larger = ord(second) if ord(first) < ord(second) else ord(first)
    res = []

    for i in range(smaller, larger+1):
        res.append(chr(i))

    return res


# 動物捕獲
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

# 最大文字列
def maxAscilString(stringList: list) -> int:
    asciList = []
    asciNumber = 0
    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            asciNumber += ord(stringList[i][j])
        asciList.append(asciNumber)
        asciNumber = 0

    return asciList.index(max(asciList))