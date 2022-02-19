from typing import List


def sort(arr: List[int], ascending: bool = True):
    for j in range(1, len(arr)):
        val = arr[j]
        i = j - 1
        while i > -1 and \
                (arr[i] > val and ascending or \
                 (arr[i] < val and not ascending)):
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = val

arr = [5, 2, 4, 6, 1, 3]
sort(arr)
assert arr == [1, 2, 3, 4, 5, 6]
sort(arr, False)
assert arr == [6, 5, 4, 3, 2, 1]
