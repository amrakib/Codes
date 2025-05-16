size = int(input())
array = input().split()
array[:] = [int(i) for i in array]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


bubble_sort(array)
for j in range(size):
    print(array[j], end=" ")
