values = int(input())
id = list(map(int, input().split()))
marks = list(map(int, input().split()))
swaps = 0
for i in range(values - 1):
    max_index = i
    for j in range(i + 1, values):
        if marks[max_index] < marks[j]:
            max_index = j
        elif marks[max_index]  == marks[j]:
            if id[max_index] > id[j]:
                max_index = j
    if i != max_index:
        marks[i], marks[max_index] = marks[max_index], marks[i]
        id[i], id[max_index] = id[max_index], id[i]
        swaps += 1
print("Minimum swaps:", swaps)
for k in range(values):
    print(f"ID: {id[k]} Mark: {marks[k]}")