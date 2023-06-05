def sumCardNumber(cardList: list):
    obj = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    sumNumber = 0
    for i in range(len(cardList)):
        sliceStr = cardList[i][1:]
        if cardList[i][1] in obj:
            sumNumber += obj[sliceStr]
        else:
            sumNumber += int(sliceStr)
    return sumNumber


def winnerBlackjack(playerCards: list, houseCards: list) -> bool:
    sumPlayerNumber = sumCardNumber(playerCards)
    sumHouseNumber = sumCardNumber(houseCards)
    if sumPlayerNumber > 21: return False
    if sumHouseNumber < 22 and sumPlayerNumber < sumHouseNumber: return False
    if sumPlayerNumber == sumHouseNumber: return False

    return True

print(winnerBlackjack(["♥10","♥6","♣K"],["♠Q","♦2","♥K"]) )

a = ["♣4","♥7","♥7"]
print(int(a[0][1]))

b = '12'
print(b[1:])


def validEmailList(emailList: list):
    validEmailList = []
    for i in range(len(emailList)):
        email = emailList[i]
        if ' ' not in email and email.count('@') == 1 and email.index('@') < email.rfind('.') and email[0] != '@':
            validEmailList.append(email)
    return validEmailList

print(validEmailList(["ccc@aaa.com","c@cc@aaa.com","cc c@aaa.com","cc.c@aaa.com"]))

a = "cc.c@aaa.com"
print(a.index('.'))

# def createAlphabetList(firstAlphabet: str, secondAlphabet: str):
#     alphabetList = []
#     for char in range(ord(firstAlphabet), ord(secondAlphabet)+1):
#         alphabetList.append(chr(char))
#     return alphabetList
#
# def generateAlphabet(firstAlphabet: str,secondAlphabet: str):
#     return createAlphabetList(firstAlphabet.lower(), secondAlphabet.lower()) if ord(firstAlphabet) <= ord(secondAlphabet) else createAlphabetList(secondAlphabet.lower(), firstAlphabet.lower())
#
# print(generateAlphabet('a','z'))
# print(generateAlphabet('b','b'))
# print(generateAlphabet('C','Z'))
# print(generateAlphabet('M','z'))
# print(generateAlphabet('z','a'))
# print(generateAlphabet('T','s'))

def createAlphabetList(firstAlphabet: str, secondAlphabet: str):
    alphabetList = []
    for char in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower())+1):
        alphabetList.append(chr(char))
    return alphabetList

def generateAlphabet(firstAlphabet: str, secondAlphabet: str):
    return createAlphabetList(firstAlphabet, secondAlphabet) if ord(firstAlphabet.lower()) <= ord(secondAlphabet.lower()) else createAlphabetList(secondAlphabet, firstAlphabet)

print(generateAlphabet('a', 'z'))
print(generateAlphabet('b', 'b'))
print(generateAlphabet('C', 'Z'))
print(generateAlphabet('M', 'z'))
print(generateAlphabet('z', 'a'))
print(generateAlphabet('T', 's'))

def generateAlphabet(firstAlphabet,secondAlphabet):
    first = firstAlphabet.lower()
    second = secondAlphabet.lower()

    smaller = ord(second) if ord(first) > ord(second) else ord(first)
    larger = ord(second) if ord(first) < ord(second) else ord(first)
    res = []

    for i in range(smaller, larger+1):
        res.append(chr(i))

    return res
