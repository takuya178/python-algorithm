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