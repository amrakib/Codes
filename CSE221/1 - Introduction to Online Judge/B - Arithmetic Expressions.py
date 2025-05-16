testcase = int(input())
for i in range(testcase):
    temp = input().split()
    first = float(temp[1])
    operator = temp[2]
    second = float(temp[3])
    if operator == "+":
        print(first + second)
    elif operator == "-":
        print(first - second)
    elif operator == "*":
        print(first * second)
    elif operator == "/":
        print(first / second)