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