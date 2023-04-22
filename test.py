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