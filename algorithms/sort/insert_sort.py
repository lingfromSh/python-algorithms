"""
将每个数向前插入到合适的位置
"""


def insert_sort(arr):
    i = 1
    while i < len(arr):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        i += 1
    return arr


if __name__ == "__main__":
    nums = [1, 23, 14, 2, 14, 124, 15, 2, 1, 231]
    r = insert_sort(nums)
    print(r)
