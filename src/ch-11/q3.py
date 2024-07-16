

from typing import List


def triangular_numbers(n: int) -> int:
    if n == 1:
        return 1
    return n + triangular_numbers(n - 1)

n = 7

print(triangular_numbers(n))