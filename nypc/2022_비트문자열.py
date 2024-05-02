def get(K, x):
    if K == 0:
        return 0
    if K > 60:
        ret = get(60, x)
        if K % 2 == 1:
            ret ^= 1
        return ret
    
    n = 1 << K
    m = n // 2
    if x > m:
        return get(K - 1, x - m)
    return get(K - 1, x) ^ 1

T = int(input())
for _ in range(T):
    K, s, e = map(int, input().split())
    ans = 0
    if e % 2 == 1:
        ans += get(K, e)
        e -= 1
    if s % 2 == 0:
        ans += get(K, s)
        s += 1
    ans += (e - s + 1) // 2
    print(ans)
