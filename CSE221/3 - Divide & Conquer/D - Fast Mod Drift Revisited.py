testcase = int(input())
for i in range(testcase):
    a, n, m = map(int, input().split())
    if a == 1:
        print(n % m)
    else:
        mod_val = m * (a - 1)
        a_pow = pow(a, n + 1, mod_val)
        numerator = (a_pow - a) % mod_val
        res = (numerator // (a - 1)) % m
        print(res)