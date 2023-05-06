def stringCompression(s):
    return stringCompressionHelper(s, 0, 0, "")

# right: leftの右側にある文字, left: 連続の始まりの文字, output: 出力する文字を格納する
def stringCompressionHelper(s, right, left, output):
    # leftが文字列の長さ以上になったら再帰を終了し、文字を格納してきたoutputを返します。
    if left >= len(s): return output
    # rightが文字列の長さ未満かつ、rightの文字とleftの文字が等しい場合、次の文字の比較に移ります
    if right < len(s) and s[right] == s[left]: return stringCompressionHelper(s, right + 1, left, output)

    # right - left で連続した値を出します
    count = right - left

    # outputに文字を加えます。文字が2以上連続していれば数字も加えます
    if count > 1: output += s[left] + str(count)
    else: output += s[left]

    # rightをleftに格納することで、連続の始まりの値を変更します。
    left = right
    return stringCompressionHelper(s, right, left, output)

def splitAndAdd(digits: int) -> int:
    return countAdd(digits, len(str(digits)), 0, 0)

def countAdd(digits: int, len_number: int, index: int, add: int) -> int:
    if len_number == index: return add
    add += (digits % 10)
    return countAdd(digits // 10, len_number, index + 1, add)

print(splitAndAdd(19))

def helperTwoTotal(n: int) -> int:
    if n == 0: return n
    return helperTwoTotal(n - 1) + n * 2

def multipleOfTwoTotal(n: int) -> int:
    if n == 0: return n
    return helperTwoTotal(n) + multipleOfTwoTotal(n - 1)

def fibonacci(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

def numberOfWay(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    return numberOfWay(x - 1) + numberOfWay(x - 2)
