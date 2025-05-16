testcase = int(input())
trains = [input().split() for _ in range(testcase)]
for i in range(len(trains) - 1):
    min_index = i
    for j in range(i + 1, len(trains)):
        if trains[min_index][0] > trains[j][0]:
            min_index = j
        elif trains[min_index][0] == trains[j][0]:
            if trains[min_index][-1] < trains[j][-1]:
                min_index = j
    temp = trains[min_index]
    while min_index > i:
        trains[min_index] = trains[min_index - 1]
        min_index -= 1
    trains[i] = temp
for k in trains:
    print(" ".join(k))