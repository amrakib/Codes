data = input().split()
size = int(data[0])
value = int(data[1])
arr = list(map(int, input().split()))
left, right = 0, size - 1
answer = -1
while left < right:
    sum = arr[left] + arr[right]
    if sum == value:
        answer = f"{left + 1} {right + 1}"
        break
    elif sum > value:
        right -= 1
    else:
        left += 1
print(answer)
