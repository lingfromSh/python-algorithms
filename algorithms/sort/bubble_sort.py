def bubble_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    swapped = True

    n, pos = len(arr), -1
    while swapped:
        swapped = False
        pos += 1
        for i in range(1, n-pos):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapped = True

    return arr


if __name__ == "__main__":
    nums = [1, 23, 14, 2, 14, 124, 15, 2, 1, 231]
    r = bubble_sort(nums)
    print(r)