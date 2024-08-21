from typing import List


def greatest_product_of_three(arr: List[int]) -> int:
    # sort in place
    arr.sort()
    return arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) - 3]

# 8 * 12 * 18 = 1728
p = greatest_product_of_three([8, 4, 2, 12, 1, 5, 18, 7, 3])
print(p)
