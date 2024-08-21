from typing import List

def find_missing_number(arr: List[int]) -> int:
    arr.sort()
    for i in range(0, len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i] + 1
    return None

m = find_missing_number([5, 2, 4, 1, 0])
print(m)
m2 = find_missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4])
print(m2)