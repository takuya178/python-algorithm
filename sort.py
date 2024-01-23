from typing import List

# Bubble sort
def bubble_sort(arr: list[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([2,5,1,8,7,3]))