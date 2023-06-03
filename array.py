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