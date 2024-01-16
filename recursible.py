# def doYouFail(string, absences=0):
#     if not string:
#         return "pass" if absences < 3 else "fail"
#
#     if string[0] == "A":
#         return doYouFail(string[1:], absences + 1)
#     else:
#         return doYouFail(string[1:], absences)
#
#
# print(doYouFail("AAPPAP"))
#
#
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
