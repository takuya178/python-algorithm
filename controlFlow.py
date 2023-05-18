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