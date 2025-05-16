size_and_k = input().split()
array = input().split()
k = int(size_and_k[1])
for i in range(k - 1, -1, -1):
    print(array[i], end=" ")
