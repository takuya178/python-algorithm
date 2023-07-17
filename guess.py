import random

def guess(min: int, max:int) -> str:
    input_num = input("数値を入力してください:")

    random_num = random.uniform(min, max)

    return "正解" if input_num == random_num else "不正解"

for i in range(5):
    print(guess(1, 10))