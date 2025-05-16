size_one = int(input())
one = input().split()
size_two = int(input())
two = input().split()
i, j = 0, 0
merged = []
while i < size_one and j < size_two:
    if int(one[i]) <= int(two[j]):
        merged.append(one[i])
        i += 1
    else:
        merged.append(two[j])
        j += 1
excess = (one, i) if i < size_one else (two, j)
print(" ".join(merged), " ".join(excess[0][excess[1] :]))

