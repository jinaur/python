import sys

n = int(sys.stdin.readline())

l = []
for i in range(0, n) :
    l.append(int(sys.stdin.readline()))

dp = [0] * n
if n <= 2 :
    print(sum(l))
else :
    dp[0] = l[0]
    dp[1] = l[0]+l[1]
    dp[2] = max(l[0]+l[1], l[0]+l[2], l[1]+l[2])
    for i in range(3, n) :
        dp[i] = max(l[i]+l[i-1]+dp[i-3], l[i]+dp[i-2], dp[i-1])

    print(max(dp))

