import math

def doYouFail(string):
    return helperDoYouFail(string, 0)

def helperDoYouFail(string: str, absence_cnt: int):
    if len(string) == 0:
        return 'fail' if absence_cnt >= 3 else 'pass'

    print(string)
    if string[0] == 'A':
        return helperDoYouFail(string[1:], absence_cnt + 1)
    else:
        return helperDoYouFail(string[1:], absence_cnt)

print(doYouFail("AAPPAP"))

def totalOfFirstAndLastDigits(n):
    if len(str(n)) == 1:
        return n

    return helperTotalOfFirstAndLastDigits(str(n), 0)

def helperTotalOfFirstAndLastDigits(n: str, count: int):
    if count == len(n):
        return int(n[0]) + int(n[-1])

    return helperTotalOfFirstAndLastDigits(n, count + 1)

print(totalOfFirstAndLastDigits(12345))

def powerXOfN(x, n):
    if n == 0:
        return 1.0

    if n > 0:
        return round(powerXOfN(x, n - 1) * x, 1)
    else:
        return round(powerXOfN(x, n + 1) / x, 1)

print(powerXOfN(2,5)) # 32
print(powerXOfN(2.1,3)) # 9.2
print(powerXOfN(2,-2)) # 0.2
print(powerXOfN(3,-7)) # 0


def infectedPeople(day):
    if day == 0:
        return 1
    return infectedPeople(day - 1) * 2

print(infectedPeople(2))


def reduceByFive(num) -> str:
    minus = helperMinusReduceByFive(num, [num])
    plus = helperPlusReduceByFive(num, minus[-1], [])
    return ', '.join(map(str, (minus+plus)))

def helperMinusReduceByFive(num, list) -> list:
    if num < 0:
        return list
    list.append(num - 5)
    return helperMinusReduceByFive(num - 5, list)

def helperPlusReduceByFive(num, min_num, list) -> list:
    if num == min_num:
        return list
    list.append(min_num + 5)
    return helperPlusReduceByFive(num, min_num + 5, list)

print(reduceByFive(16)) # 16,11,6,1,-4,1,6,11,16
