size, testcase = map(int, input().split())
arr = list(map(int, input().split()))

def search_left(arr, l, size):
    low, high = 0, size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= l:
            high = mid - 1
        else:
             low = mid + 1
    return high

def search_right(arr, h, size):
    low, high = 0, size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > h:
            high = mid - 1
        else:
            low = mid + 1
    return high

for _ in range(testcase):
    l, h = map(int, input().split())
    left = search_left(arr, l, size)
    right = search_right(arr, h, size)
    print(right - left) 