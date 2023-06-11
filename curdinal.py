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

def canMakeTargetVal(arr: list, target: int) -> bool:
    sumList = []
    for i in range(len(arr)):
        sumNum = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]: continue
            sumNum = arr[i] + arr[j]
            sumList.append(sumNum)

    return target in sumList

def canMakeTargetVal(arr,target):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target: return True
    return False


def videosToWatch(time: list, dailyGoal: int) -> int:
    goalNum = 0
    for i in range(len(time)):
        goalNum += time[i]
        if goalNum >= dailyGoal:
            return i+1

    return -1

print(videosToWatch([1,2,1,3,4],5))