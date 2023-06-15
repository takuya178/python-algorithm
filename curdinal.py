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


def characterLocation(commands: str) -> list:
    obj = {'N': 1, 'E': 1, 'W': -1, 'S': -1}
    x, y = 0, 0
    for i in range(len(commands)):
        if commands[i] == 'N':
            y += obj[commands[i]]
        elif commands[i] == 'E':
            x += obj[commands[i]]
        elif commands[i] == 'W':
            x += obj[commands[i]]
        elif commands[i] == 'S':
            y += obj[commands[i]]

    return [x, y]

def tabulationFib(n):
    # これはキャッシュであり、計算済みのフィボナッチ数をすべて保存します
    # 全てを 0 に設定します
    cache = [0] * (n+1)

    # fib0 は 0、fib1 は 1 であり、他のすべての数は fib(n) = fib(n-1) + fib(n-2) を使って求めることができます
    cache[0] = 0
    cache[1] = 1

    # 反復を使って全ての数を求めます
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]

    # n 番目のフィボナッチを返します
    return cache[n]

print(tabulationFib(50))

# 97 ~ 122
def isPangram(string: str) -> bool:
    ordList = []
    string = string.lower().replace(' ', '')
    for i in range(len(string)):
        if ord(string[i]) >= 122:
            ordList.append(ord(string[i]))

        if ordList in ord(string[i]): continue

    return True if len(ordList) == 26 else False


