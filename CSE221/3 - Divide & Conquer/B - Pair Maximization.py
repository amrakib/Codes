size = int(input())
arr = list(map(int, input().split()))
max_sum = float("-inf")
max_i = arr[0]
for j in range(1, size):
    sum = max_i + arr[j] ** 2
    if sum > max_sum:
        max_sum = sum
    if arr[j] > max_i:
        max_i = arr[j]        
print(max_sum)