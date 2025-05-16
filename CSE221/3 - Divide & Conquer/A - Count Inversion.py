def mergeSort(arr):
    if len(arr) > 1:

        left = arr[: len(arr) // 2]
        right = arr[len(arr) // 2 :]

        left_count = mergeSort(left)
        right_count = mergeSort(right)
        merge_count = merge(left, right, arr)
        return left_count + right_count + merge_count
    return 0


def merge(left, right, arr):
    i = j = k = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            count += len(left) - i
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return count


size = int(input())
arr = list(map(int, input().split()))
inversion = mergeSort(arr)
print(inversion)
print(" ".join(map(str, arr)))