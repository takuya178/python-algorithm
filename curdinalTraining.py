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