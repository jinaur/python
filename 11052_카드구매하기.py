n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1) :
    for j in range(0, i) :
        dp[i] = max(dp[i], dp[i-j-1]+p[j])

print(dp[n])

