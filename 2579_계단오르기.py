import sys
input = sys.stdin.readline

n = int(input())

l = []
for i in range(0, n) :
    l.append(int(input()))

dp = [0] * n

if n <= 2 :
    print(sum(l))
else :
    dp[0] = l[0]
    dp[1] = l[0] + l[1]
    for i in range(2, n) :
        dp[i] = max(dp[i-3] + l[i-1] + l[i], dp[i-2] + l[i])

    print(dp[len(dp)-1])

