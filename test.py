def isValidEmail(email):
    is_include_beginning_mark = email[0] == "@"
    is_not_include_mark = email.find("@") == -1
    is_include_space = " " in email
    is_duplication_mark = email.count("@") >= 2
    is_not_contain_dot_after_mark = not("." in email[email.find("@"):])

    return not (is_include_beginning_mark or is_not_include_mark or is_include_space or is_duplication_mark or is_not_contain_dot_after_mark)

import math

def middleSubstring(stringInput):
    if len(stringInput) <= 2: return stringInput[0]
    middle_number = math.floor(len(stringInput) / 2)
    remaining_number = len(stringInput) - middle_number
    even_start_number = math.floor(remaining_number / 2)
    odd_start_number = math.ceil(remaining_number / 2)

    if middle_number % 2 == 0:
        return stringInput[even_start_number:(even_start_number + middle_number)]
    else:
        return stringInput[odd_start_number:(odd_start_number + middle_number)]


def calculateLocation(latitude: float, longitude: float) -> str:
    return getLatitudeDirecton(latitude) + "/" + getLongitudeDerection(longitude);


def getLatitudeDirecton(latitude: float) -> str:
    if latitude == 0:
        return "equator"
    elif latitude >= 0.1:
        return "north"
    else:
        return "south"

def getLongitudeDerection(longitude: float) -> str:
    if longitude == 0:
        return "prime meridian"
    elif longitude >= 0.1:
        return "east"
    else:
        return "west"


def upperCaseDomain(email: string) -> string:
    start_number = email.find("@")
    return email[start_number:len(email)].upper()

def isPerfectSquare(x: int, y: int) -> bool:
    square = math.sqrt(x ** 2 + y ** 2)
    return hasDecimal(square)

def hasDecimal(x: int) -> bool:
    return not x % 1 == 0

def calculateGoalMoney(capital: int, year: int) -> int:
    if capital % 2 == 0:
        return math.floor(capital * (1.02 ** year))
    else:
        return math.floor(capital * (1.03 ** year))


def calcFallingDistance(time: int, gravitational_acceleration: int) -> int:
    return (gravitational_acceleration * (time ** 2)) / 2

def changeMile(meter: int) -> int:
    return math.floor(meter * 0.000621371)

def fallingDistance(planet: str, time: int):
    if planet == "Earth":
        return changeMile(calcFallingDistance(time, 9.8))
    elif planet == "Jupiter":
        return changeMile(calcFallingDistance(time, 24.79))
    elif planet == "Mercury":
        return changeMile(calcFallingDistance(time, 3.7))
    else:
        return 0

def isLeapYear(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def getStateTax(state: str) -> int:
    if state == "AZ":
        return 0.049
    elif state == "CA":
        return 0.0884
    elif state == "TX":
        return 0
    elif state == "NC":
        return 0.025
    else:
        return 0.05

def calcStateTax(profit: int, tax: int) -> int:
    return profit * tax

def calcFederalTax(profit: int) -> int:
    return profit * 0.21

def calculateCorporationTax(state: str, year: int, profit: int) -> int:
    if isLeapYear(year):
        return math.ceil(calcStateTax(profit, getStateTax(state)))
    else:
        return math.ceil(calcStateTax(profit, getStateTax(state)) + calcFederalTax(profit))

def isSupportedCard(creditCardType: str) -> bool:
    return creditCardType == "Visa" or creditCardType == "MasterCard"

def calcTip(cost: int) -> int:
    if cost % 3 == 0:
        return 0.03 * cost
    elif cost % 5 == 0:
        return 0.05 * cost
    elif cost % 7 == 0:
        return 0.07 * cost
    else:
        return 0.10 * cost

def calcTax(cost: int) -> int:
    tax = 0.10
    return cost * tax

def isOverCost(totalCost: int) -> bool:
    return totalCost >= 300

def processPayment(creditCardType: str, cost: int) -> int:
    if not isSupportedCard(creditCardType): return -1.0
    total_cost = cost + calcTip(cost) + calcTax(cost)
    return total_cost if not isOverCost(total_cost) else -1.0


def getGravitationalAcceleration(planet: str) -> str:
    if planet == "Earth":
        return 9.8
    elif planet == "Jupiter":
        return 24.79
    elif planet == "Mars":
        return 3.71
    elif planet == "Pluto":
        return 0.58
    elif planet == "Moon":
        return 1.62
    else:
        return 0

def calcSpeedJustBeforeGround(gravitationalAcceleration: float, height: int) -> int:
    return math.sqrt(2 * gravitationalAcceleration * height)

def getEmotion(height: int, planet: str) -> str:
    if getGravitationalAcceleration(planet) == 0: return "no data"
    speed = calcSpeedJustBeforeGround(getGravitationalAcceleration(planet), height)

    if speed >= 80:
        return "terrified"
    elif 60 <= speed <= 80:
        return "frighten"
    elif 40 <= speed < 60:
        return "scared"
    else:
        return "afraid"

def climbDownStairs(current):
    if current == 0: return 0

    return climbDownStairs(current - 1)

def multiplyOf7(number: int):
    if number == 0:
        return 0

    return multiplyOf7(number - 1) + 7


def lenString(string: str) -> int:
    if len(string) == 0:
        return 0
    return lenString(string[:-1]) + 1


def summation(n):
    if summation == 0:
        return 0
    return summation(n - 1) + n


def simpleSummation(n: str) -> str:
    if str <= 0:
        return 0
    return simpleSummation(n - 1) + n


def factorial(n: str) -> str:
    if n <= 0:
        return 1
    return factorial(n - 1) * n

def squareSummation(n: str) -> str:
    if n <= 0:
        return 0
    return squareSummation(n - 1) + n ** 2

def mergeString(s1: str, s2: str) -> str:
    if len(s1) == 0:
        return ""
    return s1[0] + s2[0] + mergeString(s1[1:], s2[1:])


def swapPosition(s):
    return helperPosition(s, len(s), 0, "")

def helperPosition(s1: str, size: int, index: int, output: str) -> str:
    if index >= size - 1:
        if size % 2 == 0:
            return output
        else:
            return output + s[-1]
    return helperPosition(s, size, index + 2, output + s[index + 1] + s[index])

def helperReachFundGoal(capitalMoney: int, goalMoney: int, interest: int, year: int) -> int:
    if capitalMoney >= goalMoney: return year

    if year >= 80: return 80

    if year % 2 == 0:
        goalMoney *= 1.02
    else:
        goalMoney *= 1.03

    return helperReachFundGoal(capitalMoney * (1 + interest / 100), goalMoney, interest, year + 1)

def howLongToReachFundGoal(capitalMoney: int, goalMoney: int, interest: int) -> int:
    return helperReachFundGoal(capitalMoney, goalMoney, interest, 0)

def helperPalindrome(s: str, index: int, result: bool) -> bool:
    if len(s) == index: return result

    reverse_s = s[::-1]
    if s[:index] == reverse_s[:index]:
        result = True
    else:
        result = False

    return helperPalindrome(s, index + 1, result)

def recursiveIsPalindrome(s: str) -> bool:
    return helperPalindrome(s.lower().replace(" ", ""), 1, False)


# フィボナッチ数列の総和
def helperFibonacci(f1: int, f2: int, n: int) -> int:
    if n < 1: return f1
    return helperFibonacci(f2, f1 + f2, n - 1)

def helperSumFibonacci(n: int) -> int:
    if n == 0: return n
    fibonacci = helperFibonacci(0, 1, n)
    return helperSumFibonacci(n - 1) + fibonacci

def fibonacciTotal(n: int) -> int:
    return helperSumFibonacci(n)

# 修正したコード
def fibonacciTotal(n):
    # 関数を完成させてください
    return helper(0,1,n,0)

def helper(fn1, fn2, n, total):
    if n < 1: return total
    return helper(fn2, fn1+fn2, n-1, total+fn2)


# 分割数字のアルゴリズム
def splitAndAdd(digits, addDigits) -> int:
    if digits == 0: return addDigits
    return splitAndAdd(digits // 10, digits % 10 + addDigits)

def totalNumber(digits, addDigits) -> int:
    if digits < 10: return addDigits
    current = splitAndAdd(digits, 0)
    return totalNumber(current, current + addDigits)

def recursiveDigitsAdded(digits: int) -> int:
    if digits < 10: return digits
    return totalNumber(digits, 0)

