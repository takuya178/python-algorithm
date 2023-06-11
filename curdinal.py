def websitePagination(urls: list, pageSize: int, page: int) -> list:
    pagenationList = []
    pageList = []
    finishNum = len(urls) % pageSize
    while len(urls) > finishNum:
        pageList.append(urls[0])
        urls = urls[1:]
        if len(pageList) == pageSize:
            pagenationList.append(pageList)
            pageList = []

    if len(urls) > 0: pagenationList.append(urls)

    return pagenationList[page-1]



def hasPenalty(records: list) -> bool:
    isPenalty = True
    while len(records) > 1:
        if records[0] < records[1] or records[0] == records[1]:
            isPenalty = False
        else:
            isPenalty = True
            break
        records = records[1:]
    return isPenalty

def isMountain(height):
    maxNumIndex = height.index(max(height))
    isHeight = True

    if maxNumIndex == 0 or maxNumIndex == len(height)-1: return False

    for i in range(maxNumIndex):
        if height[i] > height[i+1] or height[i] == height[i+1]:
            isHeight = False
            break

    for i in range(maxNumIndex, len(height)-1):
        if height[i] < height[i+1] or height[i] == height[i+1]:
            isHeight = False
            break

    return isHeight


def maxOfPairSum(arr1: list, arr2: list, x: int):
    sumList = []
    for i in range(len(arr1)):
        sumNum = 0
        for j in range(len(arr2)):
            sumNum = arr1[i] + arr2[j]
            if sumNum < x: sumList.append(sumNum)

    return max(sumList) if len(sumList) > 0 else 'no pair'

print(maxOfPairSum([2,8,7],[1,5,6],10))
print(maxOfPairSum([583,114,925,669,402,7,84,747],[655,797,905,843,652,841,893],260))
