vertices, connections = map(int, input().split())
source = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
degree = [0] * (vertices)

for i in range(connections):
    degree[source[i] - 1] += 1
    degree[end[i] - 1] += 1

odd_count = 0
for i in degree:
    if i % 2 != 0:
        odd_count += 1
        
print("YES") if odd_count in (0, 2) else print("NO")
