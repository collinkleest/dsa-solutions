

from typing import List


def total_num_of_chars(input_arr: List[str], index=0, count=0) -> int:
    if index == len(input_arr) - 1:
        return count + len(input_arr[index])
    return total_num_of_chars(input_arr, index + 1, len(input_arr[index]) + count)


input_arr = ['ab', 'c', 'def', 'ghij']

def main() -> None:
    try:
        assert total_num_of_chars(input_arr) == 10
        print(f"Test case passed.")
    except AssertionError:
        print(f"Test case failed")

main()