def isqrt(v):
    s = 1
    e = 10**9
    t = 0
    while s <= e:
        m = (s + e) // 2
        if m * m <= v:
            s = m + 1
            t = m
        else:
            e = m - 1
    return t

def solve(a, b):
    if a < b:
        return solve(b, a)
    if a == b:
        return 0
    ret = a - b
    k = isqrt(a)
    if a <= k * (k + 1):
        ret = min(ret, solve(k, b) + a - k * k + 1)
    else:
        ret = min(ret, solve(k + 1, b) + (k + 1) * (k + 1) - a + 1)
    return ret

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(solve(a, b))
 