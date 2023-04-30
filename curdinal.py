def commonPrefix(s1: str, s2: str):
    return helperPrefix(s1, s2, 0, "")


def helperPrefix(s1: str, s2: str, index: int, output: str) -> str:
    if s1[index] != s2[index] or len(s1) <= index or len(s2) <= index: return output
    return helperPrefix(s1, s2, index + 1, output + s1[index])

print(commonPrefix("abcdefg","abcxyz"))

def numberOfDots(x: int) -> int:
    return helperOfDots(x, 1, 0)

def helperOfDots(x: int, index: int, result: int) ->int:
    if x == 0: return result

    return helperOfDots(x - 1, index + 1, index + result)

def totalSquareArea(x: int) -> int:
    return helperSquareArea(x, 1, 0)

def helperSquareArea(x: int, index: int, result: int) -> int:
    if x == 0: return result
    return helperSquareArea(x - 1, index + 1, result + ((index ** 2) * index))


def sheeps(count: int) -> str:
    return helperSheeps(count, 1, '')

def helperSheeps(count: int, index:int, result: str) -> str:
    if count == 0: return result

    return helperSheeps(count - 1, index + 1, result + f"{index} sheep ~ ")

def reverseString(s: str) -> str:
    helperString(s, 0, "")

def helperString(s: str, index: int, result: str) -> str:
    if len(s) < index: return result
    return helperString(s, index + 1, result + s[index:])


b = "hello"
print(b[1:])

def reverseString(s: str) -> str:
    return helperString(s, 0, "")


def helperString(s: str, index: int, result: str) -> str:
    if len(s) <= index: return result
    return helperString(s, index + 1, s[index] + result)

print(reverseString("abcd"))

def countDivisibleByK(n: int, k: int) -> int:
    return helperDivisibleByK(n, k, 0)

def helperDivisibleByK(n: int, k: int, index: int) -> int:
    if n % k != 0: return index

    return index + helperDivisibleByK(n / k, k, index + 1)

def countMath(n: int, k: int) -> int:
    if n % k != 0: return 0
    return 1 + countMath(n / k, k)

print(countMath(30, 7))

def maximumPeople(x,y):
   if y % x == 0: return x
   return maximumPeople(y % x, y)

import math

def irreducibleFraction(x: int, y: int) -> str:
   two_gcd = twoGCD(x, y)
   if math.floor(y / two_gcd) == 1:
      return f"{math.floor(x / two_gcd)}"
   else:
      return f"{math.floor(x / two_gcd)}/{math.floor(y / two_gcd)}"

def twoGCD(x, y):
   if x % y == 0: return y
   return twoGCD(y, x % y)

print(irreducibleFraction(24, 42))