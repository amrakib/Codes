a, b = map(int, input().split())
temp = b
modlist = []
while temp > 0:
    modlist.append(temp)
    temp //= 2

temp = (a ** modlist[len(modlist) - 1]) % 107
for i in range(len(modlist) - 2, -1, -1):
    if modlist[i] == 2 * modlist[i + 1]:
        temp = (temp ** 2) % 107
    else:
        temp = (((temp ** 2) % 107) * (a % 107)) % 107
print(temp)
