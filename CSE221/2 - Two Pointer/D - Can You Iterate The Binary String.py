def find_max_in_wave(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left]

arr = [3,4,5,9,6,2,-1]
print(find_max_in_wave(arr))