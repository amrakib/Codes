def balanced_bst(arr, left, right, result):
    if left > right:
        return
    mid = (left + right) // 2
    result.append(arr[mid])
    balanced_bst(arr, left, mid - 1, result)
    balanced_bst(arr, mid + 1, right, result)


size = int(input())
arr = list(map(int, input().split()))
result = []
balanced_bst(arr, 0, size - 1, result)
print(" ".join(map(str, result)))
