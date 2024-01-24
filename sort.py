from typing import List

# Bubble sort
def bubble_sort(numbers: list[int]) -> List[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(bubble_sort([2,5,1,8,7,3]))

# Select sort
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

# Insertion sort
def insertion_sort(numbers: list[int]):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            compare_num = numbers[i]
            for j in reversed(range(i)):
                if compare_num < numbers[j]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(insertion_sort([2, 5, 1, 8, 7, 3]))
print(insertion_sort([10, 100, 1, 90, 3, 13, 45, 80, 29]))
