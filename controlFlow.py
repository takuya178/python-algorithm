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