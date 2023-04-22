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