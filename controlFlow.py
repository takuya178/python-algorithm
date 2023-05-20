# 階乗
def factorial(n: int) -> int:
    result = 1
    for i in range(n):
        print(i)
        result += i * result
        print(result)

    return result

# 修正コード
def factorial(n):
    output = 1
    for i in range(n):
        output += i * output
    return output

# 総和の総和
def summationOfSummation(n: int) -> int:
    outPut = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            outPut += j

    return outPut

print(summationOfSummation(3))

# 整数カウント
def countBetweenNumbers(digit: int, idStart: int, idEnd: int) -> int:
    outPut = 0
    for i in range(idStart, idEnd+1):
        count = list(str(i)).count(str(digit))
        outPut += count

    return outPut

# 3で割り続ける
def divideBy3Count(n: int) -> int:
    count = 0
    while not n == 1:
        n = n // 3
        count += 1
    return count

# 数字の分割
def splitAndAdd(digits: int) -> int:
    outPut = 0
    while not digits > 0:
        outPut += digits % 10
        digits = digits // 10
    return outPut


# カエサルの暗号
# POINT: 文字を文字コードに変換
def caesarCiper(message,n):
    string = message.replace(" ","")
    res = ''

    for i in string:
        # 文字は26種類なので、1文字分シフトさせた文字と27文字分シフトさせた文字は同じになります
        # そのため、26で割った余りで文字をシフトさせます
        res += converter(i, n % 26)

    return res

def converter(char, n):
    ascii = ord(char)
    shifted = ascii + n - 26 if ascii + n > 122 else ascii + n

    return chr(shifted)

# 素数
def isPrime(number: str) -> bool:
    isPrime = False
    if number == 1: return isPrime

    for i in range(2,number):
        if number % i != 0:
            isPrime = True
    return isPrime

# コードが汚かったので修正
def isPrime(number):
    for i in range(2, number) :
        if number % i == 0: return False
    return number > 1


def doYouFail(string: str) -> str:
    cnt = 0
    for i in range(len(string)):
        if string[i] == 'A': cnt += 1

    return 'pass' if cnt < 3 else 'fail'

# リファクタしたコード
def doYouFail(string):
    count = 0
    for i in string:
        if i == 'A': count += 1
        if count >= 3: return "fail"

    return "pass"
