from typing import List

# Bubble sort
def bubble_sort(numbers: list[int]) -> List[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(bubble_sort([2,5,1,8,7,3]))

# select sort
def select_sort(numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        compare_num = numbers[i]
        index = i
        for j in range(i+1, len(numbers)):
            if compare_num > numbers[j]:
                compare_num = numbers[j]
                index = j

        numbers[i], numbers[index] = numbers[index], numbers[i]

    return numbers

print(select_sort([2, 5, 1, 8, 7, 3]))
