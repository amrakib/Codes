size, k = map(int, input().split())
arr = list(map(int, input().split()))
max_length = 0
temp_sum = 0
l = 0

for r in range(size):
    temp_sum += arr[r]
    while l <= r and k < temp_sum:
        temp_sum -= arr[l]
        l += 1
    max_length = max(max_length, r - l + 1)
print(max_length)
