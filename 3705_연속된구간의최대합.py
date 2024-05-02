import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

Max = a[0]
dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i-1] + a[i])
    Max = max(Max, dp[i])

print(Max)
