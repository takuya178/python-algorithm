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
    return 0

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

# 部屋替え 難
def rotateByTimes(ids: list, n: int) -> list:
    if n == 0:
        return ids

    rotated_ids = [0] * len(ids)
    for i in range(len(ids)):
        new_index = (i + n) % len(ids)
        rotated_ids[new_index] = ids[i]

    return rotated_ids

# ページ付け
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
# ページ付け リファクタリング
def websitePagination(urls,pageSize,page):
    index = pageSize * (page - 1)
    output = []

    while index < len(urls) and pageSize > 0:
        output.append(urls[index])
        index += 1
        pageSize -= 1

    return output

# シャトルラン
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

# シャトルラン リファクタ Trueの時にループ抜ける方法の方がいいよね
def hasPenalty(records):
    for i in range(1, len(records)):
        if records[i-1] > records[i]: return True
    return False

# 山型
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

# 山型 解答
def isMountain(height):
    l = len(height)
    if l <= 0 or height[0] > height[1]: return False

    maxVal = -float('inf')
    minVal = float('inf')
    i = 0

    # 昇順が終わるまで処理を繰り返します
    while i < l and height[i] > maxVal:
        maxVal = height[i]
        i += 1

    # 昇順のみの配列の場合、falseを返します
    if i == l or max == height[i]: return False

    # 降順が終わるまで処理を繰り返します
    while i < l and height[i] < minVal:
        minVal = height[i]
        i += 1

    # 配列の末尾まで降順が続いていなかったらfalseを返します
    return i == l

# x未満の最大値
def maxOfPairSum(arr1: list, arr2: list, x: int):
    sumList = []
    for i in range(len(arr1)):
        sumNum = 0
        for j in range(len(arr2)):
            sumNum = arr1[i] + arr2[j]
            if sumNum < x: sumList.append(sumNum)

    return max(sumList) if len(sumList) > 0 else 'no pair'

# 合計値が等しい
def canMakeTargetVal(arr: list, target: int) -> bool:
    sumList = []
    for i in range(len(arr)):
        sumNum = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]: continue
            sumNum = arr[i] + arr[j]
            sumList.append(sumNum)

    return target in sumList

# 合計値が等しい リファクタリング
def canMakeTargetVal(arr,target):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target: return True
    return False

# 探索
def videosToWatch(time: list, dailyGoal: int) -> int:
    goalNum = 0
    for i in range(len(time)):
        goalNum += time[i]
        if goalNum >= dailyGoal:
            return i+1

    return -1

# パングラム
def isPangram(string: str) -> bool:
    ordList = []
    string = string.lower().replace(' ', '')
    for i in range(len(string)):
        if ord(string[i]) >= 122:
            ordList.append(ord(string[i]))

        if ordList in ord(string[i]): continue

    return True if len(ordList) == 26 else False

# パングラム キャッシュを使ったリファクタ
def isPangram(string):
    cache = [0] * 26

    for char in string:
        ascii = ord(char.lower())
        if ascii >= 97 and ascii <= 122: 
            cache[ascii - 97] = 1

    return not min(cache) == 0

# 配列のシャッフル
def shuffledPositions(arr: list, shuffledArr: list) -> list:
    result = []
    for i in range(len(shuffledArr)):
        result.append(shuffledArr.index(arr[i]))

    return result

# シャッフルの結合
import math
def shuffleSuccessRate(arr: list, shuffledArr: list) -> int:
    correct_list = []
    for i in range(len(arr)):
        if arr[i] != shuffledArr[i]:
            correct_list.append(arr[i])

    return math.floor((len(correct_list) / len(arr)) * 100)

# 配列の交点
def listIntersection(targetList: list, searchList: list) -> list:
    hash = {}
    list = []
    for i in range(len(targetList)):
        hash[targetList[i]] = targetList[i]

    for i in range(len(searchList)):
        if searchList[i] in list or not searchList[i] in hash:
            continue
        else:
            list.append(hash[searchList[i]])

    list.sort()
    return list

# モンスターの出現回数
def appearTheMost(levels: list) -> list:
    hash = {}
    list = []
    for i in range(len(levels)):
        if levels[i] in hash:
            hash[levels[i]] = hash[levels[i]]+1
        else:
            hash[levels[i]] = 1

    for i in range(len(levels)):
        if hash[levels[i]] == max(hash.values()):
            if levels[i] in list: continue
            list.append(levels[i])
    list.sort()
    return list

# アラブ人による頻度分析
def charFrequency(message):
    message = message.replace(' ', '')
    hash = {}
    list = []
    for i in range(len(message)):
        if message[i] in hash:
            hash[message[i]] = hash[message[i]]+1
        else:
            hash[message[i]] = 1

    message = ''.join(sorted(set(message)))
    for i in range(len(message)):
        list.append(f'{message[i]} : {hash[message[i]]}')

    return list

# アラブ人の解説
def charFrequency(message):
    # スペースを除きます。
    s = message.replace(' ', '')

    hashmap = {}
    res = []

    for i in range(len(s)) :        
        if s[i] not in hashmap : hashmap[s[i]] = 1
        else : hashmap[s[i]] += 1

    for key in hashmap :
        res.append(str(key) + " : " + str(hashmap[key]))

    # アルファベット順にソートします。
    return sorted(res)

# 
def twoSum(intArr: list, sumInt: list) -> list:
    list = []
    for i in range(len(intArr)):
        for j in range(i+1, len(intArr)):
            if len(list) >= 2: break
            if (intArr[i] + intArr[j] == sumInt):
                list.append(i)
                list.append(j)
    print(list)
    return list if len(list) > 0 else []

def missingItems(listA: list, listB: list) -> list:
    hash = {}
    results = []
    for i in range(len(listB)):
        hash[listB[i]] = listB[i]

    for i in range(len(listA)):
        if not listA[i] in hash: results.append(listA[i])

    return results
missingItems([1,2,3,4,5,6,7,8],[1,3,5])

def hasSameType(user1: str, user2: str):
    if len(user1) != len(user2): return False

    hash = {}
    for i in range(len(user1)):
        hash[user1[i]] = user2[i]

    values = list(hash.values())
    if len(values) == len(set(values)): return False

    for i in range(len(user1)):
        if hash[user1[i]] != user2[i]:
            return False
            break

    return True

def findPairs(numbers: list) -> list:
    hash_map = {}
    results = []
    for i in range(len(numbers)):
        if numbers[i] in hash_map:
            hash_map[numbers[i]] = hash_map[numbers[i]] + 1
        else:
            hash_map[numbers[i]] = 1

    for i in range(len(numbers)):
        if numbers[i] in results: continue
        if hash_map[numbers[i]] == 2: results.append(numbers[i])

    return sorted(results)
findPairs([10,12,13,14,15,16,16,7,7,8])

def firstNonRepeating(s: str):
    hash_map = {}
    list = []
    for i in range(len(s)):
        if s[i] in hash_map:
            hash_map[s[i]][1] += 1
        else:
            hash_map[s[i]] = [i, 1]

    for i in range(len(s)):
        if hash_map[s[i]][1] == 1:
            list.append(hash_map[s[i]][0])

    return min(list) if len(list) > 0 else -1

firstNonRepeating("aabbcdddeffg")

# 正解したが、hash_mapを使った実装の方がメモリ使用量減らせる
def getMaxLength(ranks: list) -> int:
    if len(set(ranks)) == 1:
        return 0

    player_ranks = []
    for rank in ranks:
        terms_list = []
        for i in range(len(ranks)):
            if rank == ranks[i] or rank + 1 == ranks[i]:
                terms_list.append(ranks[i])
        player_ranks.append(terms_list)

    result = 0
    for player_rank in player_ranks:
        if len(set(player_rank)) == 1:
            continue

        if len(player_rank) > result:
            result = len(player_rank)

    return result if result > 1 else 0

print(getMaxLength([1,2,2,2,1,3,4,4,4,3]))
print(getMaxLength([1,2,3,4,3,2,1,2,2,1]))
print(getMaxLength([0,0,0,0,0]))
print(getMaxLength([0,10,20,30,40]))
print(getMaxLength([0,0,2,10,6]))

