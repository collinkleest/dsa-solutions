
from typing import List


def only_even_numbers(nums_arr: List[int], evens: List[int], index=0) -> List[int]:
    if index == len(nums_arr):
        return evens

    if (nums_arr[index] % 2 == 0):
        evens.append(nums_arr[index])

    return only_even_numbers(nums_arr, evens, index + 1)

input_arr = [1, 4, 3, 2, 12, 7, 9, 14]

print(only_even_numbers(input_arr, []))

assert only_even_numbers(input_arr, []) == [4, 2, 12, 14]