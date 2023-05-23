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

# 完全数
def perfectNumberList(n: int) -> str:
    outPut = ''
    for i in range(2, n+1):
        sum_cnt = 0
        for j in range(1, i):
            if i % j == 0:
                sum_cnt += j
        if i == sum_cnt:
            outPut += str(sum_cnt) + '-'

    return outPut[:-1] if len(outPut) > 0 else 'none'

print(perfectNumberList(28))

# リファクタしたコード
import math
def perfectNumberList(n):
    numbers = ''
    for i in range(2, n+1) :
        if isPerfect(i): numbers += str(i) + '-'
    return numbers[0:-1] if numbers != '' else 'none'

# 数値を受け取って、パーフェクトナンバーかどうかチェックする関数
def isPerfect(x) :
    divisors = 1
    n = math.ceil(math.sqrt(x))
    # 約数を足し上げる（1とxを除く）
    for i in range(2, n) :
        if x % i == 0:
            divisors += i
            divisors += x / i
    return x == int(divisors)

# 素数の和
# 自分の数までで割り切れるかどうかみてる
def isPrime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def sumOfAllPrimes(n: int) -> int:
    prime_list = []
    for i in range(1, n+1):
        if isPrime(i):
            prime_list.append(i)

    return sum(prime_list)


# 10進数から16進数
def decimalToHexadecimal(decNumber: int) -> str:
    dec_number_list = ['A', 'B', 'C', 'D', 'E', 'F']
    bit = ''
    while decNumber >= 1:
        bit = (dec_number_list[(decNumber%16) - 10] if decNumber % 16 >= 10 else str(decNumber % 16)) + bit
        decNumber = decNumber // 16

    return bit

import math
def decimalToHexadecimal(decNumber):
    hexadecimal = "0123456789ABCDEF"
    hex = ''
    currentHex = 0

    while decNumber >= 0:
        currentHex = decNumber % 16
        hex = hexadecimal[currentHex] + hex
        decNumber = math.floor(decNumber/16)
        if decNumber == 0: break

    return hex