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

print(isMountain([1,2,3,2])) # True
print(isMountain([1,2]))
print(isMountain([2,1]))
print(isMountain([1,2,2,2,2]))
print(isMountain([1,2,3]) )
print(isMountain([4,3,2,1]))
print(isMountain([1,2,2,2,3,2])) # 高さは初めは上がり続ける
print(isMountain([3,2,2,2,1,1]))
print(isMountain([10,20,30,400,500,10])) # True
print(isMountain([100,200,100,400,500,100]))
print(isMountain([100,200,300,200,100,300]))
print(isMountain([100,50,100,200,300,400]))
print(isMountain([53,158,477,994,994,867,797,755,744,621,616])) # 頂点の値が同じ