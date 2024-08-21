from typing import List

# O(N)
def greatest_number1(arr: List[int]) -> int:
    g = 0
    for i in range(len(arr)):
        if arr[i] > g:
            g = arr[i]
    return g

# O(N log N)
def greatest_number2(arr: List[int]) -> int:
    arr.sort()
    return arr[len(arr) - 1]

# O(N^2)
def greatest_number3(arr: List[int]) -> int:
    pass


g1 = greatest_number1([4, 1, 2, 8, 5])
print(g1)

g2 = greatest_number2([4, 1, 2, 8, 5])
print(g2)

g3 = greatest_number3([4, 1, 2, 8, 5])
print(g3)