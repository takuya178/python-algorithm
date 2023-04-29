def commonPrefix(s1: str, s2: str):
    return helperPrefix(s1, s2, 0, "")


def helperPrefix(s1: str, s2: str, index: int, output: str) -> str:
    if s1[index] != s2[index] or len(s1) <= index or len(s2) <= index: return output
    return helperPrefix(s1, s2, index + 1, output + s1[index])

print(commonPrefix("abcdefg","abcxyz"))